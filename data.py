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


def own_data():

    patient_100_file = "/content/drive/MyDrive/Colab Notebooks/100_ekg.csv"
    ecg100 = pd.read_csv(patient_100_file, index_col=0)

    MLII = ecg100['MLII'].to_numpy()[:3600]
    V5 = ecg100['V5'].to_numpy()[:10]
    ecg100['time_ms'] = ecg100.index / 360
    time = ecg100['time_ms'].to_numpy()[:3600] 

    return MLII, time
