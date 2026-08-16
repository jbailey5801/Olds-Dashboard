import streamlit as st
import feedparser

# --------------------------------------------------
# PAGE SETTINGS
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
A personal dashboard focused on understanding long-term trends,
technology, economics, institutions, and geopolitics.

**Goal:** Read a few thoughtful pieces each week instead of chasing headlines.
""")

# --------------------------------------------------
# SIDEBAR
# --------------------------------------------------

selected_section = st.sidebar.selectbox(
    "Choose Category",
    list(sections.keys())
)

article_count = st.sidebar.slider(
    "Articles per source",
    min_value=3,
    max_value=15,
    value=5
)

# --------------------------------------------------
# WEEKLY FOCUS
# --------------------------------------------------

st.info(
    """
    📚 **Suggested Weekly Reading**

    Monday: One Our World in Data article

    Wednesday: One Works in Progress essay

    Friday: One Noahpinion or MIT Technology Review article

    Weekend: One Foreign Affairs article
    """
)

# --------------------------------------------------
# DISPLAY SELECTED SECTION
# --------------------------------------------------

feeds = sections[selected_section]

st.header(selected_section)

for source, url in feeds.items():

    with st.expander(source, expanded=False):

        feed = feedparser.parse(url)

        if not feed.entries:
            st.warning("No articles found.")
            continue

        for article in feed.entries[:article_count]:

            title = getattr(article, "title", "Untitled")

            link = getattr(article, "link", "")

            summary = getattr(article, "summary", "")

            st.markdown(
                f"### {link}"
            )

            if summary:

                clean_summary = (
                    summary
                    .replace("<p>", "")
                    .replace("</p>", "")
                    .replace("<br>", " ")
                )

                st.caption(clean_summary)

            st.divider()

# --------------------------------------------------
# FOOTER
# --------------------------------------------------

st.sidebar.markdown("---")

st.sidebar.markdown(
    """
    ### Sources

    📈 Our World in Data

    🏗 Works in Progress

    ⚙ Noahpinion

    🧪 MIT Technology Review

    🌍 Foreign Affairs
    """
)
