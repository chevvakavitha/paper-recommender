# 📚 Paper Recommender  
*A semantic research paper recommendation system using vector embeddings, FAISS similarity search, and metadata filtering.*

---

## 🌟 Overview  
The **Paper Recommender** system helps users discover research papers similar to their query or input document.  
It uses:

- **Sentence Transformers** for generating embeddings  
- **FAISS** for fast similarity search  
- **Metadata filtering** (title, author, keyword, year)  
- **Pre-computed embeddings** for instant recommendations  
- A clean, maintainable, modular architecture  

This project is useful for:  
✔ Researchers  
✔ Students  
✔ Literature Review Authors  
✔ Anyone working with large paper databases  

---

## 🚀 Features

### 🔍 Semantic Search  
Uses dense vector embeddings for high-quality paper similarity.

### ⚡ FAISS Index  
Supports fast nearest-neighbor search even with large datasets.

### 🧠 Transformer Embeddings  
Uses models like: `sentence-transformers/all-MiniLM-L6-v2`.

### 🗂 Metadata Filtering  
Filter results based on author, year, keywords, etc.

### 🧱 Modular Architecture  
Separated into `src/`, `tools/`, `data/`, `app/`.

_____________________

## 🗂 Project Structure  

paper-recommender/
│── app/ # UI app (Streamlit placeholder)
│── assets/ # Images, diagrams, demo screenshots
│── data/ # Ignored (datasets & embeddings)
│── docs/ # Documentation, notes
│── models/ # Model files (ignored)
│── notebooks/ # Jupyter notebooks for EDA
│── src/ # Core source code
│ │── init.py
│ │── app.py # Main application logic
│ │── preprocess.py # Text cleaning, metadata extraction
│ │── pdf_utils.py # PDF-to-text utilities
│ │── embed_index.py # Embedding + FAISS index builder
│ │── search.py # Search & recommendation logic
│── tools/
│ │── test_search.py # Unit tests for search
│── main.py # Project CLI entry point
│── requirements.txt # Python dependencies
│── README.md # Documentation
│── .gitignore # Ignores data/, models/, venv, etc.

__________________

## 📥 Dataset  

⚠️ The dataset was **not uploaded** because GitHub restricts files above **100 MB**.
After downloading, place the files here:
paper-recommender/data/
_______________

## 🧠 System Architecture  
User Query
↓
Preprocessing
↓
Sentence Transformer → Generate Embeddings
↓
FAISS Index → Find Similar Papers
↓
Metadata Filtering
↓
Top-K Recommended Papers
______________
## ▶️ How to Run the Project

### 1️⃣ Create virtual environment
python -m venv .venv
2️⃣ Activate environment
Windows:
.venv\Scripts\activate
Mac/Linux:
source .venv/bin/activate
3️⃣ Install dependencies
pip install -r requirements.txt
4️⃣ Run the main program
python main.py
5️⃣ (Optional) Launch Streamlit UI
streamlit run app/streamlit_app.py
______________
📝 Example Usage
python
Copy code
from src.search import PaperSearch

searcher = PaperSearch(
    embedding_path="data/papers_embeddings_meta.parquet",
    metadata_path="data/papers_metadata.csv",
    faiss_index_path="data/faiss_index.bin"
)

results = searcher.get_similar_papers("neural networks for healthcare")
print(results.head())
_______________
🛠 Technologies Used
Python 3.10+
Sentence Transformers
FAISS
Pandas / NumPy
Scikit-learn
Streamlit (optional UI)
Parquet / CSV
_________________
📌 Future Improvements
Full Streamlit dashboard with charts & explanations
PDF upload → automatic embedding
Add SHAP explanations for recommendations
Deploy model as a cloud API (FastAPI)
Topic modeling for enhanced filtering
__________________
🤝 Contributing
Contributions are welcome!
Please open an issue before major changes.
__________________
📬 Contact
Cheva Kavitha
📧 Email: kavithachevvakavitha@gmail.com
🔗 LinkedIn: www.linkedin.com/in/cheva-kavitha
__________________
⭐ Support
If you find this project useful, please give it a ⭐ star on GitHub.

