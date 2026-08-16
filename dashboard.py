import streamlit as st
import feedparser

st.title("🌎 World Intelligence Dashboard")

sources = {
    "Our World in Data":
        "https://ourworldindata.org/feed.xml",

    "Noahpinion":
        "https://www.noahpinion.blog/feed"
}

for source, url in sources.items():
    st.header(source)

    feed = feedparser.parse(url)

    for article in feed.entries[:5]:
        st.markdown(
            f"- {article.link}"
        )
