import streamlit as st
import urllib.request

url = "https://ourworldindata.org/feed.xml"

try:
    response = urllib.request.urlopen(url)

    content = response.read().decode(
        "utf-8",
        errors="ignore"
    )

    st.write(content[:2000])

except Exception as e:
    st.error(e)
