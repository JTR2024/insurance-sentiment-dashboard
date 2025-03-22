# Insurance Sentiment Dashboard (GPT-4o + Synthetic Data)

This project demonstrates how generative AI can be used to analyze sentiment in insurance-related customer feedback using synthetic data and GPT-4o. Built with Streamlit, the app allows users to:
- Explore sentiment breakdowns across 500 AI-generated insurance comments
- Filter results by company mentions
- Test GPT-4o in real time by classifying custom input

---

## What This Project Covers

- **Synthetic Data Generation**
  Created 500 realistic customer feedback comments using Python. Each entry includes metadata like company mentioned and topic discussed.

- **Sentiment Classification with GPT-4o**
  Applied OpenAI's GPT-4o to label each comment as positive, neutral, or negative using prompt-based classification.

- **Interactive Streamlit Dashboard**
  Built and deployed a responsive dashboard with filtering, charting, and real-time GPT interaction.

---

## Features

- Load and analyze 500 synthetic feedback comments
- Visualize sentiment breakdown by company
- Filter by sentiment type
- Classify new text input using GPT-4o on demand

---

## Example Use Case

This dashboard simulates an AI-assisted feedback workflow. It demonstrates how LLMs like GPT-4o can be integrated into practical sentiment analysis pipelines for customer support or product feedback applications.

---

## Tech Stack

- Python 3.10+
- Streamlit
- Pandas, Matplotlib
- OpenAI API (GPT-4o)
- GitHub + Streamlit Cloud (for deployment)

---

## Setup Instructions

1. Clone the repository:
```bash
git clone https://github.com/JTR2024/insurance-sentiment-dashboard.git
cd insurance-sentiment-dashboard
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Set your OpenAI API key:
```python
import os
os.environ["OPENAI_API_KEY"] = "your-key-here"
```

4. Launch the app locally:
```bash
streamlit run streamlit_app.py
```

## Live Demo

View the deployed dashboard here: https://insurance-sentiment-dashboard-iuuaq3ryzvet7q2eifayd6.streamlit.app

## Author

Created by JTR2024 as a demonstration of end-to-end LLM-based analysis and deployment using synthetic data.
