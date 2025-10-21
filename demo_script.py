# demo_script.py - run this to quickly test pipeline
from data import simulate_ecg
from filtering import butter_lowpass_filter, moving_average
from analysis import detect_peaks, compute_hr_and_rr, compute_hrv, classify_rhythm
from plotting import plot_raw_vs_filtered, plot_tachogram

t, raw, fs = simulate_ecg(duration=20, fs=250, heart_rate_bpm=70, noise_std=0.3, random_seed=1)
filtered = butter_lowpass_filter(raw, cutoff_hz=15, fs=fs, order=4)
smooth = moving_average(filtered, 3)
peaks, props = detect_peaks(smooth, fs, prominence=0.3)
hr, rr = compute_hr_and_rr(peaks, t)
sdnn = compute_hrv(rr)
print(f"HR: {hr:.1f} bpm, SDNN: {sdnn:.1f} ms")
plot_raw_vs_filtered(t, raw, smooth, peaks)
plot_tachogram(rr)
