
# AI-Powered Oil Well Performance Monitoring System
# I developed this project  for an oil production and servincing company and made a part of it availble on my github page for protfolio display purposes...
## Features included in the system but not added to this copy are 
1. Advanced ML
Replace Linear Regression with:
LSTM (time series deep learning)
XGBoost
2. Real-Time Data Integration
Simulate SCADA / IoT streaming
Use APIs or Kafka
3. Multi-Well Dashboard
Compare multiple wells
Rank worst-performing wells
4. Root Cause Analysis
When anomaly detected:
Pressure drop?
Temperature spike?
Suggest likely cause
5. PDF Report Generator
Auto-generate daily well reports
6. KPI Panel
Production efficiency %
Downtime prediction
Health score per well

## Features
- Production Trend Visualization
- Anomaly Detection (Isolation Forest)
- Forecasting (Linear Regression)
- Toggle between Synthetic & Real Data

## How to Run

1. Install Python (>=3.10)
2. python -m venv venv
3. venv\Scripts\activate

4. Install dependencies:
   pip install -r requirements.txt

5. Run the app:
   streamlit run app.py

6. Open browser:
   http://localhost:8501 or https://oil-well-monitoring-ai.streamlit.app/

## Real Data Format
CSV with columns:
- date
- production
- pressure
- temperature
