from openai import OpenAI
import streamlit as st
import feedparser

client = OpenAI(
    api_key=st.secrets["OPENAI_API_KEY"]
)

def analyze_article(title, summary):

    prompt = f"""
You are a geopolitical and economic analyst.

Article:
Title: {title}

Summary:
{summary}

Provide:

1. Main claim
2. Why it matters
3. Long-term implications
4. Related themes

Keep it under 150 words.
"""

    response = client.responses.create(
        model="gpt-5",
        input=prompt
    )

    return response.output_text

st.set_page_config(page_title="World Dashboard")

st.title("🌎 World Intelligence Dashboard")

sections = {

    "📈 Long-Term Trends
