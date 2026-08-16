from openai import OpenAI
import streamlit as st

client = OpenAI(
    api_key=st.secrets["OPENAI_API_KEY"]
)

st.title("OpenAI Test")

if st.button("Test AI"):

    response = client.responses.create(
        model="gpt-5",
        input="Tell me why renewable energy costs matter in 3 sentences."
    )

    st.write(response.output_text)
