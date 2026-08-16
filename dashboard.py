import streamlit as st
import feedparser
import re

# --------------------------------------------------
# PAGE CONFIG
# --------------------------------------------------

st.set_page_config(
    page_title="World Intelligence Dashboard",
    layout="wide"
)

# --------------------------------------------------
# SOURCES
# --------------------------------------------------

sections = {

    "📈 Long-Term Trends": {
        "Our World in Data":
            "https://ourworldindata.org/feed"
    },

    "🏗 Progress & Institutions": {
        "Works in Progress":
            "https://worksinprogress.co/rss.xml"
    },

    "⚙ Technology & Industry": {

        "Noahpinion":
            "https://www.noahpinion.blog/feed",

        "MIT Technology Review":
            "https://www.technologyreview.com/feed/"
    },

    "🌍 Geopolitics": {

        "Foreign Affairs":
            "https://www.foreignaffairs.com/rss.xml"
    }
}

# --------------------------------------------------
# HEADER
# --------------------------------------------------

st.title("🌎 World Intelligence Dashboard")

st.markdown("""
Read a handful of high-quality articles each week and focus on
understanding long-term trends rather than chasing headlines.
""")

# --------------------------------------------------
# SIDEBAR
# --------------------------------------------------

st.sidebar.title("Navigation")

selected_section = st.sidebar.selectbox(
    "Category",
    list(sections.keys())
)

article_count = st.sidebar.slider(
    "Articles Per Source",
    min_value=3,
    max_value=15,
    value=5
)

search_term = st.sidebar.text_input(
    "Search Titles"
)

# --------------------------------------------------
# WEEKLY READING PLAN
# --------------------------------------------------

st.info("""
📚 **Suggested Weekly Routine**

**Monday**
- Our World in Data

**Wednesday**
- Works in Progress

**Friday**
- Noahpinion or MIT Technology Review

**Weekend**
- Foreign Affairs
""")

# --------------------------------------------------
# CLEAN HTML
# --------------------------------------------------

def clean_html(text):

    if not text:
        return ""

    text = re.sub(r"<[^>]+>", "", text)
    return text

# --------------------------------------------------
# DISPLAY CONTENT
# --------------------------------------------------

feeds = sections[selected_section]

st.header(selected_section)

for source, url in feeds.items():

    with st.expander(source):

        feed = feedparser.parse(url)

        if len(feed.entries) == 0:
            st.warning(
                "Feed unavailable or no articles found."
            )
            continue

        for article in feed.entries[:article_count]:

            title = getattr(
                article,
                "title",
                "Untitled"
            )

            if search_term:
                if search_term.lower() not in title.lower():
                    continue

            link = getattr(
                article,
                "link",
                ""
            )

            summary = getattr(
                article,
                "summary",
                ""
            )

            summary = clean_html(summary)

            st.markdown(
                f"### {link}"
            )

            if summary:
                st.write(summary)

            st.divider()
        
