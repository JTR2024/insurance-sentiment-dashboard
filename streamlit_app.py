import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker

st.set_page_config(page_title="Insurance Sentiment Dashboard", layout="wide")

st.title("Insurance Sentiment Dashboard")
st.markdown("Analyze customer sentiment across synthetic insurance feedback.")

# -------------------------------
# Load and clean the data
# -------------------------------
sample_data = pd.read_csv("data/labeled_comments.csv")
sample_data = sample_data.rename(columns={"true_sentiment": "sentiment"})

sample_data['sentiment'] = (
    sample_data['sentiment']
    .str.lower()
    .str.extract(r'(positive|neutral|negative)', expand=False)
)
sample_data = sample_data.dropna(subset=["sentiment"])

# -------------------------------
# Sentiment filter
# -------------------------------
st.subheader("Sentiment Distribution")
sentiment_options = ["all"] + sorted(sample_data['sentiment'].unique())
selected_sentiment = st.selectbox("Filter by Sentiment", sentiment_options)

# Apply filter
if selected_sentiment != "all":
    filtered_data = sample_data[sample_data['sentiment'] == selected_sentiment]
else:
    filtered_data = sample_data

# -------------------------------
# Plot the chart
# -------------------------------
sentiment_counts = filtered_data['sentiment'].value_counts()

fig, ax = plt.subplots(figsize=(6, 4))
sentiment_counts.plot(kind='bar', color='skyblue', ax=ax)
ax.set_ylabel("Number of Comments")
ax.set_xlabel("Sentiment")
ax.set_title("Sentiment Distribution")
ax.yaxis.set_major_locator(ticker.MaxNLocator(integer=True))
st.pyplot(fig)