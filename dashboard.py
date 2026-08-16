import streamlit as st
import feedparser

url = "https://ourworldindata.org/feed.xml"

feed = feedparser.parse(url)

st.write("Version:", feed.get("version"))
st.write("Bozo:", feed.bozo)
st.write("Entries:", len(feed.entries))
st.write("Status:", getattr(feed, "status", "No status"))

if hasattr(feed, "bozo_exception"):
    st.write("Error:")
    st.write(feed.bozo_exception)
