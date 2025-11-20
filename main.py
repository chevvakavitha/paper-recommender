# main.py - CLI entry for preprocess, build_index, run app
import argparse
import os
import sys

# Add current directory to path so src can be imported
sys.path.insert(0, os.path.dirname(__file__))

from src.preprocess import preprocess_csv
from src.embed_index import build_embeddings_and_index

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--mode", choices=["preprocess","build_index","app"], default="app")
    parser.add_argument("--input", default="data/papers_metadata.csv")
    parser.add_argument("--parquet", default="data/papers_processed.parquet")
    parser.add_argument("--embeddings", default="data/papers_embeddings.npy")
    parser.add_argument("--index", default="data/faiss_index.bin")
    args = parser.parse_args()

    if args.mode == "preprocess":
        preprocess_csv(args.input, args.parquet)
    elif args.mode == "build_index":
        build_embeddings_and_index(args.parquet, args.index, args.embeddings)
    else:
        # Import and run app only when needed
        from src.app import run_app
        run_app()

if __name__ == "__main__":
    main()
