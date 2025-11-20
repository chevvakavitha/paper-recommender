"""Preprocessing utilities for the paper recommender.

Provides a helper to load a CSV/TSV/Parquet of paper metadata and write
out a cleaned Parquet file with a combined text field used for embeddings.

Expected columns in input: title, abstract, authors, year, pdf_link (optional)
"""
from typing import Optional
import pandas as pd


def preprocess_csv(input_path: str, output_parquet: str, text_columns: Optional[list] = None) -> None:
	"""Load metadata (CSV/Parquet), normalize columns, create `text` field and save parquet.

	Args:
		input_path: path to CSV/Parquet file containing metadata
		output_parquet: path where cleaned parquet will be written
		text_columns: list of columns to combine into the text field (default: ['title','abstract'])
	"""
	if text_columns is None:
		text_columns = ["title", "abstract"]

	if input_path.endswith(".parquet"):
		df = pd.read_parquet(input_path)
	else:
		# try CSV/TSV
		sep = ","
		if input_path.endswith(".tsv"):
			sep = "\t"
		df = pd.read_csv(input_path, sep=sep)

	# Normalize expected columns
	df = df.copy()
	for col in ["title", "abstract", "authors", "year", "pdf_link"]:
		if col not in df.columns:
			df[col] = None

	# Fill NaNs
	df["title"] = df["title"].fillna("")
	df["abstract"] = df["abstract"].fillna("")
	df["authors"] = df["authors"].fillna("")

	# Combine columns to a single text field used for embedding
	df["text"] = df[text_columns].agg(" \n ".join, axis=1)

	# Ensure year is numeric when possible
	try:
		df["year"] = pd.to_numeric(df["year"], errors="coerce").astype(pd.Int64Dtype())
	except Exception:
		# leave as-is if conversion fails
		pass

	# Add id column if missing
	if "id" not in df.columns:
		df = df.reset_index().rename(columns={"index": "id"})

	df.to_parquet(output_parquet, index=False)


if __name__ == "__main__":
	import argparse

	parser = argparse.ArgumentParser()
	parser.add_argument("input")
	parser.add_argument("output")
	args = parser.parse_args()
	preprocess_csv(args.input, args.output)

