# Insurance Sentiment Dashboard

**Live App**: [https://insurance-sentiment-dashboard-iuuaq3ryzvet7q2eifayd6.streamlit.app](#)

## Overview
This project demonstrates how generative AI can be used to simulate and analyze customer sentiment in the insurance industry using synthetic data and a GPT-4o classifier.

**Features**:
- **Synthetic Data Generation**: Realistic insurance feedback is created using prompt engineering.
- **Sentiment Classification**: GPT-4o labels each feedback comment as positive, neutral, or negative.
- **Interactive Dashboard**: A Streamlit application for exploring sentiment trends and trying live GPT-4o classification.

## Architecture
*(Insert a simple flow diagram here if possible.)*

1. **Synthetic Feedback** → 
2. **GPT-4o Sentiment Analysis** → 
3. **Data Storage & Processing** → 
4. **Streamlit Visualization**

## Background
Initially a notebook-based workflow (`SentimentAnalysis.ipynb`), the project has grown into a full-stack, Streamlit-powered web application. Over 500 synthetic comments were generated and labeled for sentiment, company names, and discussion topics.

## Setup and Usage
1. **Clone the repo**:
    ```bash
    git clone https://github.com/JTR2024/insurance-sentiment-dashboard.git
    cd insurance-sentiment-dashboard
    ```
2. **Install dependencies**:
    ```bash
    pip install -r requirements.txt
    ```
3. **Configure API key**:
    ```python
    import os
    os.environ["OPENAI_API_KEY"] = "your-key-here"
    ```
4. **Run the app locally**:
    ```bash
    streamlit run streamlit_app.py
    ```
5. **Visit the Live App**:  
   [Streamlit App](https://insurance-sentiment-dashboard-iuuaq3ryzvet7q2eifayd6.streamlit.app)

## Dashboard Features
- **Company-Level Sentiment**: A bar chart that breaks down sentiment per company and updates with filters.
- **Real-Time Classification**: Input any text, and GPT-4o classifies sentiment immediately.

*(Add screenshots or GIFs if possible.)*

## Notebooks
- `SentimentAnalysis.ipynb` in `/archive/`:  
  - Synthetic data generation  
  - GPT-4o annotation process  
  - Exploratory data analysis

## Performance & Metrics
*(If available, provide a summary of the sentiment model’s accuracy or an example confusion matrix.)*

## Future Directions
- Integration with RAG for context-based Q&A
- Automated CI/CD pipeline (GitHub Actions)
- Enhanced performance evaluation & error analysis

## Contributing
Contributions are welcome! Please open a pull request or file an issue.

## License
This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details.

---

**Author**: JTR2024  
Built as a full-stack LLM pipeline demo for generative AI and insurance sentiment analysis.
