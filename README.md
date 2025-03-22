# 📊 Insurance Sentiment Dashboard (GPT-4o + Synthetic Data)

This project demonstrates how Generative AI can be used to analyze sentiment in customer feedback — specifically in the insurance industry — using synthetic data and a GPT-4o-powered classifier.

Built with **Streamlit**, this app presents a live dashboard where users can:
- Explore sentiment breakdowns across 500 AI-generated insurance comments
- Filter sentiment by company mentions
- Try GPT-4o on their own custom comment input

---

## 🧠 What This Project Shows

- **Synthetic Data Generation**  
  Used Python to simulate 500 realistic insurance-related customer feedback comments, along with metadata such as company mentions and discussion topics.

- **Sentiment Classification Using GPT-4o**  
  Each comment was classified using OpenAI’s GPT-4o via prompt-based interaction, assigning `positive`, `neutral`, or `negative` labels.

- **Streamlit Dashboard Deployment**  
  A clean UI for exploring sentiment by company, visualizing sentiment distribution, and testing GPT on-the-fly with new input.

---

## 🚀 Features

- 📁 Analyzes a dataset of 500 synthetic insurance feedback comments  
- 🏷 Sentiment classification: **positive**, **neutral**, **negative**  
- 🏢 Company filter for focused analysis (e.g. Allstate, USAA, Progressive)  
- 📈 Bar chart showing sentiment breakdown by selected company  
- 🧪 GPT-4o prompt interface to classify new comments in real time

---

## 💡 Example Use Case

This dashboard could be used to:
- Simulate an **AI-driven sentiment pipeline** for customer feedback
- Showcase **LLM integration** in data workflows
- Test how language affects **perceived sentiment** in support conversations

---

## 🛠 Tech Stack

- Python 3.10+
- Streamlit
- Pandas, Matplotlib
- OpenAI GPT-4o API
- GitHub + Streamlit Cloud (deployment)

---

## 📦 Setup

1. Clone this repo:
   ```bash
   git clone https://github.com/JTR2024/insurance-sentiment-dashboard.git
   cd insurance-sentiment-dashboard
