import os
import sys

# Ensure project root on path so src can be imported
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
if ROOT not in sys.path:
    sys.path.insert(0, ROOT)

from src.search import search_index

queries = [
    "attention mechanisms",
    "time series forecasting",
    "language models",
    "anomaly detection in time series",
    "data analyst"
]

for q in queries:
    print('\n=== Query:', q)
    try:
        results = search_index(q, 'data/faiss_index.bin', 'data/papers_embeddings_meta.parquet', top_k=5, rerank=False)
        for i, r in enumerate(results, 1):
            print(f"{i}. {r.get('title','')}  (score={r.get('score',0):.4f})")
    except Exception as e:
        print('Search error:', e)
