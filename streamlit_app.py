import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker

st.set_page_config(page_title="Insurance Sentiment Dashboard", layout="wide")

st.title("Insurance Sentiment Dashboard")
st.markdown("""
This project simulates an AI-driven workflow for analyzing customer feedback in the insurance industry.  
It uses 500 synthetic comments to demonstrate how large language models (LLMs) can be applied for sentiment classification and data exploration.  
Use the dashboard to explore sentiment by company.
""")

# Load and clean data
sample_data = pd.read_csv("data/labeled_comments.csv")
sample_data = sample_data.rename(columns={"true_sentiment": "sentiment"})

sample_data['sentiment'] = (
    sample_data['sentiment']
    .str.lower()
    .str.extract(r'(positive|neutral|negative)', expand=False)
)
sample_data = sample_data.dropna(subset=["sentiment"])

st.markdown(f"Analyzing {len(sample_data)} total comments.")

# Filter by company
st.subheader("Sentiment by Company")
company_options = ["All"] + sorted(sample_data['company_mentioned'].dropna().unique())
selected_company = st.selectbox("Select a company", company_options)

if selected_company == "All":
    filtered_data = sample_data
else:
    filtered_data = sample_data[sample_data['company_mentioned'] == selected_company]

# Sentiment counts and chart
sentiment_counts = filtered_data['sentiment'].value_counts().reindex(
    ['positive', 'neutral', 'negative'], fill_value=0
)

fig, ax = plt.subplots(figsize=(4, 2.5))
sentiment_counts.plot(kind='bar', color='skyblue', ax=ax)
ax.set_ylabel("Number of Comments")
ax.set_xlabel("Sentiment")
ax.set_title(f"Sentiment for {selected_company if selected_company != 'All' else 'All Companies'}")
ax.yaxis.set_major_locator(ticker.MaxNLocator(integer=True))
st.pyplot(fig)