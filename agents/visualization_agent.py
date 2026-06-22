import plotly.express as px

def sales_by_product_chart(df):

    if "Product" in df.columns and "Sales" in df.columns:

        sales_data = (
            df.groupby("Product")["Sales"]
            .sum()
            .reset_index()
        )

        fig = px.bar(
            sales_data,
            x="Product",
            y="Sales",
            title="Sales by Product"
        )

        return fig

    return None


def sales_by_region_chart(df):

    if "Region" in df.columns and "Sales" in df.columns:

        region_data = (
            df.groupby("Region")["Sales"]
            .sum()
            .reset_index()
        )

        fig = px.pie(
            region_data,
            names="Region",
            values="Sales",
            title="Region Wise Sales"
        )

        return fig

    return None