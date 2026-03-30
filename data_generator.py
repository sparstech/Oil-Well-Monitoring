
import pandas as pd
import numpy as np

def generate_data(n_days=365):
    np.random.seed(42)
    dates = pd.date_range(end=pd.Timestamp.today(), periods=n_days)

    production = 1000 + np.sin(np.linspace(0, 20, n_days))*100 + np.random.normal(0, 30, n_days)
    pressure = 3000 + np.random.normal(0, 50, n_days)
    temperature = 80 + np.random.normal(0, 5, n_days)

    # Inject anomalies
    for i in range(0, n_days, 50):
        production[i] *= np.random.uniform(0.5, 0.7)

    df = pd.DataFrame({
        "date": dates,
        "production": production,
        "pressure": pressure,
        "temperature": temperature
    })

    return df
