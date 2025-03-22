import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import openai

st.set_page_config(page_title="Insurance Sentiment Dashboard", layout="wide")

st.title("Insurance Sentiment Dashboard")
st.markdown("""
This dashboard analyzes 500 synthetic insurance-related feedback comments.
Each comment was classified by GPT-4o as positive, neutral, or negative.
Use the filters and tools below to explore sentiment by company or test your own text.
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

# Show total
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

fig, ax = plt.subplots(figsize=(5, 3.5))
sentiment_counts.plot(kind='bar', color='skyblue', ax=ax)
ax.set_ylabel("Number of Comments")
ax.set_xlabel("Sentiment")
ax.set_title(f"Sentiment for {selected_company if selected_company != 'All' else 'All Companies'}")
ax.yaxis.set_major_locator(ticker.MaxNLocator(integer=True))
st.pyplot(fig)

# GPT-4o input block
st.subheader("Classify a New Comment")

example = "The claims process was very slow and unhelpful."
user_input = st.text_area("Enter a customer comment:", placeholder=example)

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

if st.button("Classify Comment"):
    if user_input.strip() == "":
        st.warning("Please enter a comment.")
    else:
        with st.spinner("Classifying..."):
            result = classify_sentiment(user_input)
        st.success(f"Sentiment: {result}")