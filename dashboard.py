from openai import OpenAI
import streamlit as st
import feedparser

client = OpenAI(
    api_key=st.secrets["OPENAI_API_KEY"]
)

def analyze_article(title, summary):

    prompt = f"""
You are a geopolitical and economic analyst.

Article:
Title: {title}

Summary:
{summary}

Provide:

1. Main claim
2. Why it matters
3. Long-term implications
4. Related themes

Keep it under 150 words.
"""

    response = client.responses.create(
        model="gpt-5",
        input=prompt
    )

    return response.output_text
    
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
        
                title = article.title
        
                summary = getattr(
                    article,
                    "summary",
                    ""
                )

                st.markdown(f"### {title}")

        if summary:
            st.caption(summary)

        if st.button(
            f"Analyze: {title}",
            key=f"{source}_{title}"
        ):

            with st.spinner(
                "Analyzing..."
            ):

                analysis = analyze_article(
                    title,
                    summary
                )


        for article in feed.entries[:5]:

            st.markdown(
                f"- {article.link}"
            )
def analyze_article(title, summary):

    prompt = f"""
You are a geopolitical and economic analyst.

Article:
Title: {title}

Summary:
{summary}

Provide:

1. Main claim
2. Why it matters
3. Long-term implications
4. Related themes

Keep it under 150 words.
"""

    response = client.responses.create(
        model="gpt-5",
        input=prompt
    )

    return response.output_text
