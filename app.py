
import streamlit as st
import pandas as pd
import plotly.express as px
from data_generator import generate_data
from model_utils import detect_anomalies, forecast

st.title("AI-Powered Oil Well Monitoring")

mode = st.sidebar.radio("Select Data Mode", ["Synthetic Data", "Upload Real Data"])

if mode == "Synthetic Data":
    df = generate_data()
else:
    uploaded_file = st.file_uploader("Upload CSV")
    if uploaded_file:
        df = pd.read_csv(uploaded_file)
    else:
        st.stop()

st.subheader("Raw Data")
st.write(df.head())

# Trends
st.subheader("Production Trend")
fig = px.line(df, x="date", y="production")
st.plotly_chart(fig)

# Anomaly Detection
df = detect_anomalies(df)
st.subheader("Anomaly Detection")
fig2 = px.scatter(df, x="date", y="production", color="anomaly")
st.plotly_chart(fig2)

# Forecast
st.subheader("Forecast (Next 30 Days)")
preds = forecast(df)
forecast_df = pd.DataFrame({"Day": range(len(preds)), "Forecast": preds})
fig3 = px.line(forecast_df, x="Day", y="Forecast")
st.plotly_chart(fig3)
