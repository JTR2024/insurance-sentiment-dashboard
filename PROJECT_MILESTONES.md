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

## 🔜 Milestone 4: Streamlit App Integration & Deployment

- [ ] Add real-time user input for GPT-based sentiment classification
- [ ] Add GPT Q&A section using RAG
- [ ] Display charts and filters interactively
- [ ] Add `requirements.txt`, `Procfile`, and runtime config
- [ ] Configure GitHub Actions for CI
- [ ] Deploy to AWS or Streamlit Cloud

---

## 🧠 Bonus: Future Enhancements

- [ ] Replace synthetic data with real customer feedback
- [ ] Add multi-label or aspect-based sentiment
- [ ] Fine-tune model on insurance-specific language