import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import openai

# -------------------------------
# Streamlit Config & Header
# -------------------------------
st.set_page_config(page_title="Insurance Sentiment Demo", layout="wide")
st.title("📊 Insurance Sentiment Dashboard")
st.markdown("""
This dashboard explores **500 synthetic customer feedback comments** generated to simulate insurance-related discussions.  
All comments were classified using **GPT-4o** into sentiment categories.  
Use the charts and tools below to explore the data or test GPT's classification on your own text.
""")

# -------------------------------
# Load Data & Rename Columns
# -------------------------------
try:
    df = pd.read_csv("data/labeled_comments.csv")
    df = df.rename(columns={"true_sentiment": "sentiment"})
except FileNotFoundError:
    st.error("CSV not found at data/labeled_comments.csv")
    st.stop()

# Clean and normalize sentiment
df['sentiment'] = (
    df['sentiment']
    .str.lower()
    .str.extract(r'(positive|neutral|negative)', expand=False)
)
df = df.dropna(subset=["sentiment"])

st.markdown(f"📄 Currently analyzing **{len(df)} comments**")

# -------------------------------
# Sentiment by Company Chart
# -------------------------------
st.subheader("📊 Sentiment Breakdown by Company")

selected_company = st.selectbox(
    "Filter by Company Mentioned",
    options=["All"] + sorted(df['company_mentioned'].dropna().unique())
)

if selected_company == "All":
    filtered = df
else:
    filtered = df[df['company_mentioned'] == selected_company]

sentiment_counts = filtered['sentiment'].value_counts().reindex(['positive', 'neutral', 'negative'], fill_value=0)

fig, ax = plt.subplots(figsize=(5, 3.5))
sentiment_counts.plot(kind='bar', color='skyblue', ax=ax)
ax.set_title(f"Sentiment for {selected_company if selected_company != 'All' else 'All Companies'}")
ax.set_ylabel("Number of Comments")
ax.yaxis.set_major_locator(ticker.MaxNLocator(integer=True))
st.pyplot(fig)

# -------------------------------
# GPT-4o Live Sentiment Classifier
# -------------------------------
st.subheader("🧠 Try GPT-4o Sentiment Classification")

example = "I'm still waiting to hear back about my claim, it's frustrating."
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
        with st.spinner("Asking GPT-4o..."):
            result = classify_sentiment(user_input)
        st.success(f"**Sentiment:** {result}")