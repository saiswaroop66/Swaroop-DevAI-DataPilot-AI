import streamlit as st

from agents.loader_agent import load_data
from agents.cleaning_agent import clean_data

from agents.analytics_agent import (
    get_kpis,
    top_customers,
    top_products
)

from agents.visualization_agent import (
    sales_by_product_chart,
    sales_by_region_chart
)

from agents.report_agent import generate_report
from agents.chat_agent import ask_business_question
from agents.forecast_agent import forecast_sales

# --------------------------------
# PAGE CONFIG
# --------------------------------

st.set_page_config(
    page_title="Swaroop DevAI – DataPilot AI",
    page_icon="📊",
    layout="wide"
)

# --------------------------------
# TITLE
# --------------------------------

st.title("📊 Swaroop DevAI – DataPilot AI")
st.subheader("AI Business Intelligence Agent")

# --------------------------------
# FILE UPLOAD
# --------------------------------

uploaded_file = st.file_uploader(
    "Upload CSV File",
    type=["csv"]
)

# --------------------------------
# MAIN APP
# --------------------------------

if uploaded_file is not None:

    try:
        df = load_data(uploaded_file)
        clean_df = clean_data(df)

        st.success("✅ File Uploaded Successfully")

        # --------------------------------
        # DATA PREVIEW
        # --------------------------------

        st.subheader("📋 Dataset Preview")
        st.dataframe(clean_df)

        # --------------------------------
        # DATASET INFO
        # --------------------------------

        st.subheader("📊 Dataset Information")

        col1, col2, col3 = st.columns(3)

        col1.metric("Rows", clean_df.shape[0])
        col2.metric("Columns", clean_df.shape[1])
        col3.metric(
            "Missing Values",
            int(clean_df.isnull().sum().sum())
        )

        # --------------------------------
        # KPI DASHBOARD
        # --------------------------------

        st.subheader("📈 Business KPIs")

        kpis = get_kpis(clean_df)

        c1, c2, c3 = st.columns(3)

        c1.metric(
            "Total Sales",
            f"${kpis.get('Total Sales',0):,.0f}"
        )

        c2.metric(
            "Total Profit",
            f"${kpis.get('Total Profit',0):,.0f}"
        )

        c3.metric(
            "Total Orders",
            kpis.get("Total Orders",0)
        )

        # --------------------------------
        # TOP CUSTOMERS
        # --------------------------------

        st.subheader("🏆 Top Customers")

        customers = top_customers(clean_df)

        if customers is not None:
            st.dataframe(customers)

        # --------------------------------
        # TOP PRODUCTS
        # --------------------------------

        st.subheader("📦 Top Products")

        products = top_products(clean_df)

        if products is not None:
            st.dataframe(products)

        # --------------------------------
        # CHARTS
        # --------------------------------

        st.subheader("📊 Sales by Product")

        product_chart = sales_by_product_chart(clean_df)

        if product_chart is not None:
            st.plotly_chart(
                product_chart,
                use_container_width=True
            )

        st.subheader("🌍 Region Wise Sales")

        region_chart = sales_by_region_chart(clean_df)

        if region_chart is not None:
            st.plotly_chart(
                region_chart,
                use_container_width=True
            )

        # --------------------------------
        # AI REPORT
        # --------------------------------

        st.subheader("🤖 AI Business Report")

        if st.button("Generate AI Report"):

            with st.spinner("Generating Report..."):

                report = generate_report(clean_df)

                st.markdown(report)

        # --------------------------------
        # AI CHAT ANALYST
        # --------------------------------

        st.subheader("💬 AI Business Analyst")

        question = st.text_input(
            "Ask anything about your business data"
        )

        if st.button("Ask AI"):

            if question:

                with st.spinner("Analyzing..."):

                    answer = ask_business_question(
                        clean_df,
                        question
                    )

                    st.write(answer)

        # --------------------------------
        # SALES FORECAST
        # --------------------------------

        st.subheader("🔮 Sales Forecast")

        if st.button("Predict Future Sales"):

            prediction = forecast_sales(clean_df)

            st.success(prediction)

        # --------------------------------
        # AVAILABLE COLUMNS
        # --------------------------------

        st.subheader("📌 Available Columns")

        st.write(list(clean_df.columns))

    except Exception as e:
        st.error(f"Error: {e}")

else:
    st.info("👆 Upload a CSV file to start analysis")
