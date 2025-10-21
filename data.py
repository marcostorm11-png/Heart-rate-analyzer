# data.py
"""
Data acquisition and simulation utilities.
Member A responsibility.
"""

import numpy as np
import pandas as pd

def simulate_ecg(duration=10, fs=250, heart_rate_bpm=70, noise_std=0.2, random_seed=None):
    """
    Simulate a simple ECG-like waveform for testing.
    Returns: t (s), signal (unitless), fs
    """
    if random_seed is not None:
        np.random.seed(random_seed)
    t = np.linspace(0, duration, int(duration * fs), endpoint=False)
    # create a repeated pulse-like waveform using a sum of sinusoids
    hr = heart_rate_bpm / 60.0
    # base sinusoid at heart-rate frequency to mimic beat periodicity
    base = 1.0 * np.sin(2 * np.pi * hr * t)
    # small higher harmonics to make shapes slightly non-sinusoidal
    harm = 0.25 * np.sin(2 * np.pi * 2 * hr * t) + 0.1 * np.sin(2 * np.pi * 3 * hr * t)
    # occasional sharper R-peaks: add gaussian pulses every beat
    signal = base + harm
    beat_times = np.arange(0, duration, 1.0/hr)
    for bt in beat_times:
        # add a narrow gaussian spike at beat time
        sigma = 0.01
        signal += 1.0 * np.exp(-0.5 * ((t - bt)/sigma)**2)
    # add noise
    signal += noise_std * np.random.randn(len(t))
    return t, signal, fs

def load_csv_ecg(path, column=None):
    """
    Load ECG data from a CSV file. Assumes each row is a time sample or each row is an ECG segment.
    If CSV is a single-row-per-segment dataset (like some Kaggle sets), return first row as 1D signal.
    If the CSV contains time and signal columns, auto-detect.
    """
    df = pd.read_csv(path, header=None)
    # Try typical shapes: if df has one row and many columns, return that row
    if df.shape[0] == 1 and df.shape[1] > 1:
        return df.iloc[0].values
    # else if many rows and 1 or 2 columns, return first numeric column
    if df.shape[1] == 1:
        return df.iloc[:,0].values
    # fallback: return first row
    return df.iloc[0].values

# optional: helper to load PhysioNet with wfdb
def load_wfdb_record(record_name, pn_dir='mitdb'):
    try:
        import wfdb
    except Exception as e:
        raise RuntimeError("wfdb required for PhysioNet reading. pip install wfdb") from e
    record = wfdb.rdrecord(record_name, pn_dir=pn_dir)
    # record.p_signal is shape (nsamples, n_leads)
    sig = record.p_signal[:,0]  # first channel
    fs = record.fs
    return np.arange(len(sig)) / fs, sig, fs
