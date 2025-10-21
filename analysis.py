# analysis.py
"""
Peak detection and HR/HRV calculations.
Member C responsibility.
"""

import numpy as np
from scipy.signal import find_peaks

def detect_peaks(signal, fs, min_bpm=30, max_bpm=220, prominence=0.3, distance_s=0.4):
    """
    Detect R-peaks (or PPG peaks) using scipy.find_peaks.
    Returns array of indices of peaks.
    distance_s: minimum distance between peaks in seconds (avoid double-detection)
    """
    distance_samples = int(distance_s * fs)
    peaks, properties = find_peaks(signal, distance=distance_samples, prominence=prominence)
    return peaks, properties

def compute_hr_and_rr(peaks, t):
    """
    Given peak indices and t array (s), compute heart rate (bpm) and RR intervals (s).
    t: time array in seconds
    peaks: indices into t
    Returns: hr_bpm (float), rr_intervals (1D array in s)
    """
    if len(peaks) < 2:
        return 0.0, np.array([])
    times = t[peaks]
    rr = np.diff(times)  # seconds
    hr = 60.0 / np.mean(rr)
    return hr, rr

def compute_hrv(rr_intervals_s):
    """
    Compute simple HRV metrics. Return SDNN in ms.
    """
    if rr_intervals_s.size == 0:
        return np.nan
    sdnn = np.std(rr_intervals_s) * 1000.0  # ms
    return sdnn

def classify_rhythm(hr_bpm, hrv_sdnn_ms, hr_threshold=(40, 110), hrv_threshold=150):
    """
    Simple rule-based classification:
    - 'bradycardia' if hr < hr_threshold[0]
    - 'tachycardia' if hr > hr_threshold[1]
    - 'irregular' if hrv_sdnn_ms > hrv_threshold
    - else 'normal'
    """
    if hr_bpm == 0:
        return "no-detection"
    if hr_bpm < hr_threshold[0]:
        return "bradycardia"
    if hr_bpm > hr_threshold[1]:
        return "tachycardia"
    if hrv_sdnn_ms > hrv_threshold:
        return "irregular"
    return "normal"
