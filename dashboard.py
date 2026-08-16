import streamlit as st
import feedparser

st.title("OWID Test")

feed = feedparser.parse(
    "https://ourworldindata.org/feed"
)

st.write("Entries:", len(feed.entries))
