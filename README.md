# Insurance Sentiment Dashboard

**Live App**: https://insurance-sentiment-dashboard-iuuaq3ryzvet7q2eifayd6.streamlit.app

## Overview

This project demonstrates how generative AI can be used to simulate and analyze customer sentiment in the insurance industry. It uses synthetic data and GPT-4o for classification, and presents the results in an interactive dashboard. It includes:
- A custom data pipeline for generating realistic insurance feedback
- Sentiment classification using GPT-4o
- A Streamlit dashboard for exploring sentiment trends by company

## Features

- **Synthetic Data Generation**: 500 insurance feedback comments created using prompt engineering and randomized templates
- **Sentiment Classification**: Each comment is labeled as positive, neutral, or negative using OpenAI's GPT-4o
- **Interactive Dashboard**: Streamlit app to filter by company and view sentiment breakdowns

## Architecture

Synthetic Feedback → GPT-4o Sentiment Analysis → Data Storage → Streamlit Visualization

## Background

This project began as a Jupyter notebook workflow (`SentimentAnalysis.ipynb`) for generating synthetic insurance feedback and using GPT-4o to annotate sentiment. That work was later transitioned into a web app using Streamlit.

## Setup and Usage

1. Clone the repo:
   ```bash
   git clone https://github.com/JTR2024/insurance-sentiment-dashboard.git
   cd insurance-sentiment-dashboard
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Run the app locally:
   ```bash
   streamlit run streamlit_app.py
   ```

## Dashboard Highlights

- **Company-Level Sentiment**: A bar chart that filters sentiment by company
- **Fully Self-Contained**: No API key required; classification is pre-processed for privacy and reproducibility

## Notebooks

The original notebook (`SentimentAnalysis.ipynb`) is located in `/archive/` and includes:
- Synthetic data generation
- GPT-4o annotation process
- Exploratory data analysis
- A retrieval-augmented generation (RAG) function using TF-IDF to retrieve relevant comments before GPT classification

This notebook represents the foundation of the project. The deployed dashboard showcases only a portion of that work.

## Status

This project is considered complete as a standalone demo of GPT-powered sentiment analysis using synthetic insurance data.

## License

This project is licensed under the MIT License.

**Author**: JTR2024  
Originally developed as a full-stack LLM pipeline demo for generative AI and insurance feedback analysis.
