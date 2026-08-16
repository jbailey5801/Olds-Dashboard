import streamlit as st
import feedparser

st.title("Feed Test")

feed = feedparser.parse(
    "https://ourworldindata.org/feed.xml"
)

for article in feed.entries[:5]:
    st.write(article.title)
