import streamlit as st
import feedparser

st.set_page_config(page_title="World Dashboard")

st.title("🌎 World Intelligence Dashboard")

sections = {

    "📈 Long-Term Trends": {
        "Our World in Data":
            "https://ourworldindata.org/feed.xml"
    },

    "🏗 Progress & Institutions": {
        "Works in Progress":
            "https://worksinprogress.co/feed"
    },

    "⚙ Technology & Industry": {

        "Noahpinion":
            "https://www.noahpinion.blog/feed",

        "MIT Technology Review":
            "https://www.technologyreview.com/feed/"
    }
}

for category, feeds in sections.items():

    st.header(category)

    for source, url in feeds.items():

        with st.expander(source):

    feed = feedparser.parse(url)

    for article in feed.entries[:5]:

        st.markdown(
            f"- {article.link}"
        )

        feed = feedparser.parse(url)

        for article in feed.entries[:5]:

            st.markdown(
                f"- {article.link}"
            )
