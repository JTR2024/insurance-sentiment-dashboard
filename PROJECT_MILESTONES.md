# 📍 Project Milestones: Insurance Sentiment Dashboard

## ✅ Milestone 0: Project Bootstrap & Environment Setup

- [x] Initialized Git repository and pushed to GitHub
- [x] Created folder structure (`notebooks/`, `data/`, `app/`)
- [x] Added `.gitignore`, `README.md`, and `requirements.txt`
- [x] Created and activated Python virtual environment
- [x] Installed all dependencies locally via `pip`
- [x] Signed into GitHub and configured remote origin
- [x] Moved `SentimentAnalysis.ipynb` into `notebooks/`

---

## ✅ Milestone 1: Sentiment Classification

- [x] Extracted GPT-4o sentiment classification logic from notebook
- [x] Converted logic into reusable function: `classify_sentiment(text)`
- [x] Manually validated sentiment labels from sample outputs
- [x] Successfully tested multiple sample inputs with GPT-4o

---

## ✅ Milestone 2: Retrieval-Augmented Generation (RAG)

- [x] Built TF-IDF retrieval function: `retrieve_relevant_comments()`
- [x] Wrapped GPT-4o into RAG pipeline: `answer_with_context(query)`
- [x] Tested RAG function with sample feedback and queries

---

## ✅ Milestone 3: Data Visualization in Streamlit

- [x] Created `streamlit_app.py` and launched local dashboard
- [x] Loaded real labeled data from CSV
- [x] Cleaned and normalized sentiment labels
- [x] Rendered sentiment distribution bar chart
- [x] Added interactive sentiment filter

---

## ✅ Milestone 4: Streamlit App Integration

- [x] Added GPT-4o input to classify new user-submitted comment
- [x] Displayed response inline below the chart
- [x] Fully functional local UI using synthetic data

---

## ✅ Milestone 5: Deployment Pipeline

- [x] Created and committed `Procfile` for deployment
- [x] Added `requirements.txt` and verified dependencies
- [x] Committed `labeled_comments.csv` for cloud access
- [x] Deployed working app to Streamlit Cloud
- [x] Cleaned up diagnostics post-deploy

---

## 🧠 Bonus: Future Enhancements

- [ ] Replace synthetic data with real customer feedback
- [ ] Add multi-label or aspect-based sentiment
- [ ] Fine-tune model on insurance-specific language