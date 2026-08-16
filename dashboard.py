import streamlit as st
import feedparser

st.set_page_config(page_title="World Dashboard")

st.title("🌎 World Intelligence Dashboard")

sources = {
    "📈 Our World in Data":
        "https://ourworldindata.org/feed.xml",

    "🏗 Works in Progress":
        "https://worksinprogress.co/feed",

    "⚙ Noahpinion":
        "https://www.noahpinion.blog/feed",

    "🧪 MIT Technology Review":
        "https://www.technologyreview.com/feed/"
}

for source_name, feed_url in sources.items():

    st.header(source_name)

    feed = feedparser.parse(feed_url)

    for article in feed.entries[:5]:
        st.markdown(
            f"- {article.link}"
        )
