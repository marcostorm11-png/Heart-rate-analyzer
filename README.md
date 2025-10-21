# Heart Rate & Signal Processing Analyzer

## Quick start
1. Create a virtual environment: `python -m venv venv && source venv/bin/activate`
2. Install requirements: `pip install -r requirements.txt`
3. Run notebook: `jupyter lab` and open `demo.ipynb`
4. Or run the demo script: `python demo_script.py`

## Files
- `data.py` : simulate and load ECG/PPG data
- `filtering.py` : Butterworth & moving average filters
- `analysis.py` : peak detection, HR/HRV computation, classifier
- `plotting.py` : plotting helpers
- `demo.ipynb` : end-to-end demonstration
- `examples/` : place sample CSV files here

## Team
- Member A: data.py
- Member B: filtering.py
- Member C: analysis.py
- Member D: plotting, writeup, integration
