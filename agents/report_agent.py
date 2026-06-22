from utils.llm import ask_llm

def generate_report(df):

    data_summary = df.head(20).to_string()

    prompt = f"""
    You are a Senior Business Analyst.

    Analyze this business data:

    {data_summary}

    Generate:

    1. Executive Summary
    2. Key Findings
    3. Business Insights
    4. Recommendations

    Keep it professional.
    """

    return ask_llm(prompt)