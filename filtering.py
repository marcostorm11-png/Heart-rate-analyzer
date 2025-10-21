# filtering.py
"""
Filter utilities: moving average and Butterworth lowpass filter.
Member B responsibility.
"""

import numpy as np
from scipy.signal import butter, filtfilt

def moving_average(signal, window_size=5):
    """
    Simple moving average smoothing.
    """
    if window_size <= 1:
        return signal.copy()
    kernel = np.ones(window_size) / window_size
    # pad to keep same length
    padded = np.pad(signal, (window_size//2, window_size-1-window_size//2), mode='edge')
    smoothed = np.convolve(padded, kernel, mode='valid')
    return smoothed

def butter_lowpass_filter(signal, cutoff_hz, fs, order=4):
    """
    Zero-phase Butterworth lowpass filter via filtfilt.
    cutoff_hz: cutoff frequency in Hz
    fs: sampling frequency in Hz
    """
    nyq = 0.5 * fs
    Wn = float(cutoff_hz) / nyq
    if Wn >= 1.0:
        # no filtering
        return signal.copy()
    b, a = butter(order, Wn, btype='low')
    filtered = filtfilt(b, a, signal)
    return filtered
