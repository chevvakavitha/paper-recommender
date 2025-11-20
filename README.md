📚 Paper Recommender

A semantic research paper recommendation system using transformer embeddings and FAISS vector search.

<p align="center"> <img src="https://img.shields.io/badge/Python-3.10+-blue?style=for-the-badge" /> <img src="https://img.shields.io/badge/FAISS-Vector_Search-orange?style=for-the-badge" /> <img src="https://img.shields.io/badge/Transformers-Embeddings-green?style=for-the-badge" /> <img src="https://img.shields.io/badge/Streamlit-UI-red?style=for-the-badge" /> </p>

📑 Table of Contents
Overview
Features
Project Structure
Architecture
Dataset
Installation
Usage
Future Improvements
Contact

🌟 Overview
The Paper Recommender helps users discover research papers based on semantic similarity rather than simple keywords.
It uses:
🧠 Sentence Transformer embeddings
⚡ FAISS vector index for fast similarity search
🗂 Metadata filtering (year, author, keywords)
🏗 Modular & clean architecture

Ideal for:
Students
Researchers
Literature review writers
Anyone exploring academic content

🚀 Features
🔍 Semantic Search
Find meaningful similar papers using transformer-based sentence embeddings.
⚡ FAISS Vector Index
Fast KNN search over thousands of embeddings.
🧠 Transformer Embeddings
Uses models like:
sentence-transformers/all-MiniLM-L6-v2
🧱 Modular Architecture
Separated into src/, data/, tools/, models/.

🎛 Metadata Filters
Filter by:
Author
Year
Keywords

🗂 Project Structure
paper-recommender/
│── app/                        # (Optional) Streamlit UI 
│── assets/                     # Banner / screenshots
│── data/                       # Ignored (large datasets)
│── docs/                       # Additional documentation
│── models/                     # Trained models (ignored)
│── notebooks/                  # EDA & experimentation
│── src/                        
│   │── app.py                  # Core application logic
│   │── preprocess.py           # Cleaning & normalization
│   │── pdf_utils.py            # Optional PDF-to-text
│   │── embed_index.py          # Build embeddings & FAISS index
│   │── search.py               # Main search functions
│── tools/
│   │── test_search.py          # Unit tests
│── main.py                     # CLI entry point
│── requirements.txt            # Dependencies
│── README.md                   # Documentation
│── .gitignore                  # Ignoring large folders

🧠 Architecture
                   ┌───────────────────────┐
                   │     User Query        │
                   └──────────┬────────────┘
                              ↓
                     Preprocessing Module
                              ↓
              Sentence Transformer Model
                   (Embeddings Generation)
                              ↓
                       FAISS Index
                 (Top-K Vector Search)
                              ↓
                  Metadata Filtering Layer
                              ↓
               Final Ranked Paper Results

📥 Dataset
⚠️ GitHub blocks files bigger than 100 MB, so the dataset is stored externally.
After download, place the files in:
paper-recommender/data/

🛠 Installation
1️⃣ Create Virtual Environment
python -m venv .venv
2️⃣ Activate Environment
Windows
.venv\Scripts\activate
Mac/Linux
source .venv/bin/activate
3️⃣ Install Requirements
pip install -r requirements.txt
▶️ Usage
Run CLI version:
python main.py
Run Streamlit UI (Optional):
streamlit run app/streamlit_app.py

Minimal Python Example:
from src.search import PaperSearch

searcher = PaperSearch(
    embedding_path="data/papers_embeddings_meta.parquet",
    metadata_path="data/papers_metadata.csv",
    faiss_index_path="data/faiss_index.bin"
)

results = searcher.get_similar_papers("neural networks for healthcare")
print(results.head())

📌 Future Improvements
📄 PDF upload + automatic embedding
🌐 Full Streamlit dashboard
🔍 Add keyword extraction & topic modeling
🧠 Explain recommendations using SHAP
☁️ Deploy as FastAPI web service
🧪 Add proper unit tests

📬 Contact

Cheva Kavitha
📧 Email:  kavithachevvakavitha@gmail.com
🔗 LinkedIn:  www.linkedin.com/in/cheva-kavitha

⭐ If you like this project, consider giving it a star on GitHub!



