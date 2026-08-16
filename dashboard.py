import streamlit as st
import feedparser

st.title("OWID Feed Test")

url = "https://ourworldindata.org/feed.xml"

feed = feedparser.parse(url)

st.write("Feed Version:", feed.get("version"))
st.write("Bozo:", feed.bozo)
st.write("Number of Entries:", len(feed.entries))

for article in feed.entries[:5]:
    st.write(article.title)
