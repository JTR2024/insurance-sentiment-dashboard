import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import openai
import os

# -------------------------------
# Streamlit Config & Header
# -------------------------------
st.set_page_config(page_title="Insurance Sentiment Dashboard", layout="wide")
st.title("📊 Insurance Sentiment Dashboard")
st.markdown("Analyze customer sentiment across synthetic insurance feedback.")

# -------------------------------
# Load CSV Data
# -------------------------------
try:
    sample_data = pd.read_csv("data/labeled_comments.csv")
    sample_data = sample_data.rename(columns={"true_sentiment": "sentiment"})
except FileNotFoundError:
    st.error("CSV not found at data/labeled_comments.csv")
    st.stop()

# -------------------------------
# Clean and Normalize Sentiment
# -------------------------------
sample_data['sentiment'] = (
    sample_data['sentiment']
    .str.lower()
    .str.extract(r'(positive|neutral|negative)', expand=False)
)
sample_data = sample_data.dropna(subset=["sentiment"])

# -------------------------------
# Sentiment Distribution + Filter
# -------------------------------
st.subheader("Sentiment Distribution")
sentiment_options = ["all"] + sorted(sample_data['sentiment'].unique())
selected_sentiment = st.selectbox("Filter by Sentiment", sentiment_options)

if not selected_sentiment or selected_sentiment == "all":
    filtered_data = sample_data
else:
    filtered_data = sample_data[sample_data['sentiment'] == selected_sentiment]

# Plot chart with fixed Y-axis and better size
fig, ax = plt.subplots(figsize=(6, 4))
sentiment_counts = filtered_data['sentiment'].value_counts()
sentiment_counts.plot(kind='bar', color='skyblue', ax=ax)

ax.set_ylabel("Number of Comments")
ax.set_xlabel("Sentiment")
ax.set_title("Sentiment Distribution")
ax.yaxis.set_major_locator(ticker.MaxNLocator(integer=True))
ax.set_ylim(0, sentiment_counts.max() + 1)

st.pyplot(fig)

# -------------------------------
# GPT-4o Live Sentiment Classifier
# -------------------------------
st.subheader("🔍 Classify a New Comment")

def classify_sentiment(text: str) -> str:
    try:
        response = openai.chat.completions.create(
            model="gpt-4o",
            messages=[
                {
                    "role": "user",
                    "content": f"Classify the sentiment of the following insurance-related feedback as positive, negative, or neutral:\n\n{text}"
                }
            ],
            max_tokens=10,
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        return f"Error: {e}"

user_input = st.text_area("Enter a customer comment:")

if st.button("Classify Sentiment"):
    if user_input.strip() == "":
        st.warning("Please enter a comment first.")
    else:
        with st.spinner("Classifying..."):
            sentiment_result = classify_sentiment(user_input)
        st.success(f"**Sentiment:** {sentiment_result}")