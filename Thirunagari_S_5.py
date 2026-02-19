# EcoTrek Solutions — Week 5 Web Presentation (Streamlit)
# Option 2 (Vibe Coding) — with clear rubric labels

import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
from wordcloud import WordCloud

# ===== RUBRIC: TITLE =====
st.set_page_config(page_title="EcoTrek Review Dashboard", layout="wide")
st.title("EcoTrek Solutions — Customer Review Sentiment Dashboard")

# ===== RUBRIC: PAGE DESCRIPTION =====
st.write("""
This interactive dashboard summarizes EcoTrek Solutions customer reviews by sentiment
(**positive**, **neutral**, **negative**). It includes:
- Review counts by sentiment
- Word clouds for each sentiment category
""")

# ---- Load data (CSV should be in the same repo folder) ----
DATA_FILE = "Thirunagari_Samay_sentiment.csv"
df = pd.read_csv(DATA_FILE)

# Try common column names
df.columns = [c.strip() for c in df.columns]
sentiment_col = "Sentiment" if "Sentiment" in df.columns else "sentiment"
review_col = "Review" if "Review" in df.columns else "review"

# Normalize sentiment text
df[sentiment_col] = df[sentiment_col].astype(str).str.strip().str.lower()

# ===== RUBRIC: VISUALIZATIONS — counts =====
st.subheader("Review Counts by Sentiment")
counts = df[sentiment_col].value_counts().reindex(["positive", "neutral", "negative"]).fillna(0).astype(int)

fig = plt.figure(figsize=(6, 4))
plt.bar(counts.index, counts.values)
plt.xlabel("Sentiment")
plt.ylabel("Number of Reviews")
plt.title("Customer Reviews by Sentiment")
st.pyplot(fig)

st.divider()

# ===== RUBRIC: VISUALIZATIONS — word clouds =====
st.subheader("Word Clouds by Sentiment")

def wc_fig(text: str, title: str):
    wc = WordCloud(width=900, height=450, background_color="white", collocations=False).generate(text)
    f = plt.figure(figsize=(9, 4.5))
    plt.imshow(wc, interpolation="bilinear")
    plt.axis("off")
    plt.title(title)
    return f

c1, c2, c3 = st.columns(3)

with c1:
    st.markdown("### Positive")
    txt = " ".join(df[df[sentiment_col] == "positive"][review_col].dropna().astype(str))
    st.pyplot(wc_fig(txt if txt.strip() else "No positive reviews", "Positive Reviews"))

with c2:
    st.markdown("### Neutral")
    txt = " ".join(df[df[sentiment_col] == "neutral"][review_col].dropna().astype(str))
    st.pyplot(wc_fig(txt if txt.strip() else "No neutral reviews", "Neutral Reviews"))

with c3:
    st.markdown("### Negative")
    txt = " ".join(df[df[sentiment_col] == "negative"][review_col].dropna().astype(str))
    st.pyplot(wc_fig(txt if txt.strip() else "No negative reviews", "Negative Reviews"))
