
from sklearn.ensemble import IsolationForest
from sklearn.linear_model import LinearRegression
import numpy as np

def detect_anomalies(df):
    model = IsolationForest(contamination=0.05)
    df["anomaly"] = model.fit_predict(df[["production", "pressure", "temperature"]])
    return df

def forecast(df, days=30):
    df = df.reset_index(drop=True)
    X = np.arange(len(df)).reshape(-1,1)
    y = df["production"].values

    model = LinearRegression()
    model.fit(X, y)

    future_X = np.arange(len(df), len(df)+days).reshape(-1,1)
    preds = model.predict(future_X)

    return preds
