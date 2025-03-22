# Insurance Sentiment Dashboard

This project demonstrates how generative AI can be used to simulate and analyze customer sentiment in the insurance industry using synthetic data and a GPT-4o classifier. It includes:
- A data generation pipeline that creates synthetic insurance customer feedback
- Sentiment classification using OpenAI GPT-4o
- A deployed Streamlit dashboard to explore and interact with the results

---

## Background

This project began as a notebook-based workflow where I:
- Generated 500 synthetic insurance-related customer feedback comments using prompt engineering and randomized templates
- Annotated each comment using GPT-4o to classify sentiment as positive, neutral, or negative
- Captured metadata like company mentioned and topic discussed for each comment

The notebook (`SentimentAnalysis.ipynb`) is included in the repo.

---

## What the Dashboard Does

The dashboard builds on that work and provides:
- A company-level sentiment breakdown across 500 GPT-labeled comments
- A bar chart visualization that updates when filtered
- A live GPT-4o input to classify new customer feedback in real time

---

## Use Cases

This project simulates a realistic workflow for:
- Applying LLMs to customer feedback pipelines
- Exploring synthetic data for modeling or prototyping
- Demonstrating prompt-based classification in a web app

---

## Tech Stack

- Python 3.10+
- Streamlit
- OpenAI GPT-4o API
- Pandas, Matplotlib
- GitHub + Streamlit Cloud

---

## Setup

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

## Live App

View the deployed app here: https://insurance-sentiment-dashboard-iuuaq3ryzvet7q2eifayd6.streamlit.app

## Notebooks

The original notebook that generated the data and applied GPT classification is included in the `/archive/` folder.

## Author

Built by JTR2024 as a full-stack LLM pipeline demo for generative AI and insurance sentiment analysis.
