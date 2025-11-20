"""Search utilities: query FAISS index and return ranked results.

Supports optional CrossEncoder reranking when available.
"""
from typing import List, Optional, Dict, Any
import numpy as np
import pandas as pd
from sentence_transformers import SentenceTransformer
import faiss

try:
	from cross_encoder import CrossEncoder
except Exception:
	CrossEncoder = None


def load_index(index_path: str):
	return faiss.read_index(index_path)


def search_index(query: str, index_path: str, meta_parquet: str, model_name: str = "all-MiniLM-L6-v2", top_k: int = 10, year_range: Optional[List[int]] = None, keywords: Optional[List[str]] = None, rerank: bool = True) -> List[Dict[str, Any]]:
	df = pd.read_parquet(meta_parquet)

	model = SentenceTransformer(model_name)
	q_emb = model.encode([query], convert_to_numpy=True)
	q_emb = q_emb / np.linalg.norm(q_emb, axis=1, keepdims=True)

	index = load_index(index_path)
	distances, indices = index.search(q_emb.astype(np.float32), top_k)
	distances = distances[0]
	indices = indices[0]

	results = []
	for idx, score in zip(indices, distances):
		if idx < 0 or idx >= len(df):
			continue
		row = df.iloc[int(idx)].to_dict()
		row_score = float(score)
		row.update({"score": row_score})
		results.append(row)

	# Apply year filter
	if year_range is not None:
		start, end = year_range
		results = [r for r in results if (r.get("year") is None) or (pd.isna(r.get("year")) or (start <= int(r.get("year")) <= end))]

	# Apply keyword filter (simple contains in title/abstract)
	if keywords:
		kws = [k.strip().lower() for k in keywords if k.strip()]
		def contains_kws(r):
			txt = (str(r.get("title", "")) + " \n " + str(r.get("abstract", ""))).lower()
			return all(k in txt for k in kws)
		results = [r for r in results if contains_kws(r)]

	# Optionally rerank with CrossEncoder for better accuracy
	if rerank and CrossEncoder is not None and len(results) > 0:
		pairs = [[query, (r.get("title","") + "\n" + r.get("abstract",""))] for r in results]
		reranker = CrossEncoder("cross-encoder/ms-marco-MiniLM-L-6-v2")
		rerank_scores = reranker.predict(pairs)
		for r, s in zip(results, rerank_scores):
			r["rerank_score"] = float(s)
		results = sorted(results, key=lambda r: r.get("rerank_score", r.get("score", 0)), reverse=True)

	return results


if __name__ == "__main__":
	import argparse

	parser = argparse.ArgumentParser()
	parser.add_argument("--index", default="data/faiss_index.bin")
	parser.add_argument("--meta", default="data/papers_embeddings_meta.parquet")
	parser.add_argument("--q", default="transformers for time series")
	args = parser.parse_args()
	res = search_index(args.q, args.index, args.meta)
	import json
	print(json.dumps(res[:10], indent=2))

