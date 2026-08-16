feed = feedparser.parse(
2
"https://ourworldindata.org/feed"
3
)
4
5
st.write("Entries:", len(feed.entries))
