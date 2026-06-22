import pandas as pd

def get_kpis(df):

    kpis = {}

    # Total Sales
    if "Sales" in df.columns:
        kpis["Total Sales"] = df["Sales"].sum()

    # Total Profit
    if "Profit" in df.columns:
        kpis["Total Profit"] = df["Profit"].sum()

    # Total Orders
    kpis["Total Orders"] = len(df)

    return kpis


def top_customers(df):

    if "Customer" in df.columns and "Sales" in df.columns:

        result = (
            df.groupby("Customer")["Sales"]
            .sum()
            .sort_values(ascending=False)
            .head(5)
        )

        return result

    return None


def top_products(df):

    if "Product" in df.columns and "Sales" in df.columns:

        result = (
            df.groupby("Product")["Sales"]
            .sum()
            .sort_values(ascending=False)
            .head(5)
        )

        return result

    return None