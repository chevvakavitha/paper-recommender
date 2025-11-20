"""Build embeddings and FAISS index from processed metadata.

Saves:
- FAISS index file
- Numpy embeddings (.npy)
- metadata parquet with id -> row mapping
"""
from typing import Optional
import os
import numpy as np
import pandas as pd
from sentence_transformers import SentenceTransformer
import faiss


def build_embeddings_and_index(parquet_path: str, index_path: str, embeddings_path: str, model_name: str = "all-MiniLM-L6-v2") -> None:
	"""Load processed parquet, compute embeddings and build a FAISS index.

	Args:
		parquet_path: path to parquet with columns ['id','text',...]
		index_path: path to write faiss index binary
		embeddings_path: path to write numpy embeddings (.npy)
		model_name: sentence-transformers model
	"""
	df = pd.read_parquet(parquet_path)
	texts = df["text"].fillna("").astype(str).tolist()

	model = SentenceTransformer(model_name)
	embeddings = model.encode(texts, show_progress_bar=True, convert_to_numpy=True)

	# Normalize to unit vectors for cosine similarity via dot product
	norms = np.linalg.norm(embeddings, axis=1, keepdims=True)
	norms[norms == 0] = 1.0
	embeddings = embeddings / norms

	d = embeddings.shape[1]
	index = faiss.IndexFlatIP(d)  # inner product on normalized vectors => cosine similarity
	index.add(embeddings)

	# Ensure output dir
	os.makedirs(os.path.dirname(index_path) or ".", exist_ok=True)

	faiss.write_index(index, index_path)
	np.save(embeddings_path, embeddings)

	# Save metadata copy (ensures id mapping preserved)
	meta_out = os.path.splitext(embeddings_path)[0] + "_meta.parquet"
	df.to_parquet(meta_out, index=False)


if __name__ == "__main__":
	import argparse

	parser = argparse.ArgumentParser()
	parser.add_argument("parquet")
	parser.add_argument("index")
	parser.add_argument("embeddings")
	parser.add_argument("--model", default="all-MiniLM-L6-v2")
	args = parser.parse_args()
	build_embeddings_and_index(args.parquet, args.index, args.embeddings, model_name=args.model)
