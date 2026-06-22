import pandas as pd

def forecast_sales(df):

    if "Sales" not in df.columns:
        return "Sales column not found"

    avg_sales = df["Sales"].mean()

    prediction = round(avg_sales * 1.05, 2)

    return f"Predicted Next Month Sales: ${prediction}"