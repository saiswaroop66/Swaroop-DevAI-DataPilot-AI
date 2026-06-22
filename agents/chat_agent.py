from utils.llm import ask_llm

def ask_business_question(df, question):

    data = df.head(50).to_string()

    prompt = f"""
    You are an expert Business Intelligence Analyst.

    Dataset:

    {data}

    User Question:
    {question}

    Give a professional business answer.
    """

    return ask_llm(prompt)