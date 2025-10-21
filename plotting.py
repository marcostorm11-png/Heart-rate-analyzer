# plotting.py
"""
Plotting utilities.
Member D responsibility.
"""

import matplotlib.pyplot as plt
import numpy as np

def plot_raw_vs_filtered(t, raw, filtered, peaks=None, fs=None, title="Raw vs Filtered Signal"):
    plt.figure(figsize=(12,4))
    plt.plot(t, raw, label='Raw', alpha=0.5)
    plt.plot(t, filtered, label='Filtered', linewidth=1.2)
    if peaks is not None and len(peaks) > 0:
        plt.plot(t[peaks], filtered[peaks], 'ro', label='Detected peaks')
    plt.xlabel("Time (s)")
    plt.ylabel("Amplitude")
    plt.title(title)
    plt.legend()
    plt.tight_layout()
    plt.show()

def plot_tachogram(rr_s):
    """
    RR intervals in ms as a function of beat number
    """
    if len(rr_s) == 0:
        print("No RR intervals to plot.")
        return
    plt.figure(figsize=(8,3))
    plt.plot(np.arange(1, len(rr_s)+1), rr_s*1000.0, marker='o')
    plt.xlabel("Beat index")
    plt.ylabel("RR interval (ms)")
    plt.title("Tachogram (RR intervals)")
    plt.grid(True)
    plt.tight_layout()
    plt.show()

def histogram_rr(rr_s):
    if len(rr_s) == 0:
        return
    plt.figure(figsize=(6,3))
    plt.hist(rr_s*1000.0, bins=20, edgecolor='black')
    plt.xlabel("RR interval (ms)")
    plt.ylabel("Count")
    plt.title("Histogram of RR intervals")
    plt.tight_layout()
    plt.show()
