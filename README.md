# 📚 Paper Recommender
*A semantic research paper recommendation system using transformer embeddings and FAISS vector search.*

<p align="center">
  <img src="assets/banner.png" width="100%" />
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.10+-blue?style=for-the-badge" />
  <img src="https://img.shields.io/badge/FAISS-Vector_Search-orange?style=for-the-badge" />
  <img src="https://img.shields.io/badge/Transformers-Embeddings-green?style=for-the-badge" />
  <img src="https://img.shields.io/badge/Streamlit-UI-red?style=for-the-badge" />
</p>

---

## 📑 Table of Contents
- [Overview](#overview)
- [Features](#features)
- [Project Structure](#project-structure)
- [Architecture](#architecture)
- [Dataset](#dataset)
- [Installation](#installation)
- [Usage](#usage)
- [Future Improvements](#future-improvements)
- [Contact](#contact)

---

## 🌟 Overview
The **Paper Recommender** helps users discover relevant research papers using semantic embeddings instead of simple text matching.

It uses:
- 🧠 Sentence Transformer embeddings  
- ⚡ FAISS vector index for fast similarity search  
- 🗂 Metadata filtering (year, author, keywords)  
- 🏗 Clean modular architecture  

This project is useful for:
- Researchers  
- Students  
- Literature review writers  
- Anyone working with academic data  

---

## 🚀 Features

### 🔍 Semantic Search
High-quality semantic matching using Transformer embeddings.

### ⚡ FAISS Vector Index
Efficient KNN search across thousands of embeddings.

### 🧠 Transformer Embeddings
Uses:  
```
sentence-transformers/all-MiniLM-L6-v2
```

### 🎛 Metadata Filters
Filter by:
- Author  
- Year  
- Keywords  

### 🧱 Modular Architecture
Clean folder structure for maintainability.

---

## 🗂 Project Structure

```
paper-recommender/
│── app/                        # (Optional) Streamlit UI 
│── assets/                     # Banner / screenshots
│── data/                       # Ignored (large datasets)
│── docs/                       # Additional documentation
│── models/                     # Trained models (ignored)
│── notebooks/                  # EDA & experimentation
│── src/                        
│   │── app.py                  # Core app
│   │── preprocess.py           # Cleaning & normalization
│   │── pdf_utils.py            # PDF-to-text utilities
│   │── embed_index.py          # Embeddings + FAISS index builder
│   │── search.py               # Search logic
│── tools/
│   │── test_search.py          # Unit test
│── main.py                     # CLI entry point
│── requirements.txt            # Dependencies
│── README.md                   # Documentation
│── .gitignore                  # Ignore large folders
```

---

## 🧠 Architecture

```
User Query
     ↓
Preprocessing
     ↓
Sentence Transformer (Embeddings)
     ↓
FAISS Index (Top-K Search)
     ↓
Metadata Filtering Layer
     ↓
Final Ranked Papers
```

---

## 📥 Dataset

⚠️ The dataset exceeds GitHub's 100MB limit.

Download it manually:

```
<ADD_YOUR_GOOGLE_DRIVE_LINK_HERE>
```

Place the dataset in:

```
paper-recommender/data/
```

---

## 🛠 Installation

### 1️⃣ Create Virtual Environment
```
python -m venv .venv
```

### 2️⃣ Activate Environment  
**Windows:**
```
.venv\Scripts\activate
```
**Mac/Linux:**
```
source .venv/bin/activate
```

### 3️⃣ Install Requirements
```
pip install -r requirements.txt
```

---

## ▶️ Usage

### CLI Version:
```
python main.py
```

### Streamlit UI:
```
streamlit run app/streamlit_app.py
```

### Example:
```python
from src.search import PaperSearch

searcher = PaperSearch(
    embedding_path="data/papers_embeddings_meta.parquet",
    metadata_path="data/papers_metadata.csv",
    faiss_index_path="data/faiss_index.bin"
)

results = searcher.get_similar_papers("neural networks for healthcare")
print(results.head())
```

---

## 📌 Future Improvements
- Full Streamlit dashboard  
- Topic modeling integration  
- PDF upload + automatic embedding  
- Deploy using FastAPI  
- Add SHAP explanations  

---

## 📬 Contact
**Cheva Kavitha**  
📧 Email: kavithachevvakavitha@gmail.com  
🔗 LinkedIn: www.linkedin.com/in/cheva-kavitha 

⭐ If this project helped you, please give it a **star**!






