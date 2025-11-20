"""Streamlit dashboard for the Paper Recommender.

Features:
- Text search
- Upload PDF and search by its content
- Filters: year range, keywords, top-k
"""


import streamlit as st
from typing import Optional
import os
import sys

# Handle imports for both direct run and package imports
try:
    from .pdf_utils import extract_text_from_pdf
    from .search import search_index
except ImportError:
    from pdf_utils import extract_text_from_pdf
    from search import search_index


DEFAULT_INDEX = os.path.join("data", "faiss_index.bin")
DEFAULT_META = os.path.join("data", "papers_embeddings_meta.parquet")


def run_app():
	st.set_page_config(page_title="AI Paper Recommender", layout="wide", initial_sidebar_state="expanded")
	
	# Custom styling
	st.markdown("""
		<style>
		.main-header { font-size: 2.5rem; color: #1f77b4; font-weight: bold; }
		.result-card { background: #f0f2f6; padding: 1rem; border-radius: 0.5rem; margin-bottom: 1rem; }
		.similarity-score { color: #27ae60; font-weight: bold; font-size: 1.1rem; }
		</style>
	""", unsafe_allow_html=True)
	
	st.markdown('<p class="main-header">🔍 AI-Powered Research Paper Recommender</p>', unsafe_allow_html=True)
	st.markdown("Find similar papers based on **semantic meaning** — not just keywords.")
	
	# Initialize session state for search results
	if "search_results" not in st.session_state:
		st.session_state.search_results = None
	if "last_query" not in st.session_state:
		st.session_state.last_query = None

	with st.sidebar:
		st.header("⚙️ Search Configuration")
		model_name = st.selectbox("Embedding model", ["all-MiniLM-L6-v2"], index=0, help="Model used for semantic embeddings")
		top_k = st.selectbox("Top results", [5, 10, 20, 50], index=1, help="Number of papers to retrieve")
		year_range = st.slider("Year range", 1990, 2030, (2015, 2025), help="Filter results by publication year")
		keywords = st.text_input("Keywords filter (comma separated)", "", help="Optional: only show papers containing these words")
		rerank = st.checkbox("Enable cross-encoder rerank", value=True, help="Re-rank results for higher accuracy (slower)")
		
		st.markdown("---")
		st.markdown("**How it works:**")
		st.markdown("1. Enter a query or upload a PDF")
		st.markdown("2. Click **Search** or use the query directly")
		st.markdown("3. Results are ranked by semantic similarity")

	# Two-column layout for search input
	col1, col2 = st.columns([3, 1])
	
	with col1:
		query = st.text_input("📝 Enter a research question, topic, or keywords", placeholder="e.g., 'transformers for time series'")
	
	with col2:
		search_button = st.button("🔎 Search", use_container_width=True)

	# PDF upload section
	st.markdown("---")
	st.subheader("📄 Or upload a PDF to find similar papers")
	uploaded_file = st.file_uploader("Upload a research paper PDF", type=["pdf"], help="Extract abstract/content and find similar papers")
	
	pdf_query = None
	if uploaded_file is not None:
		with st.spinner("📖 Extracting text from PDF..."):
			try:
				pdf_text = extract_text_from_pdf(uploaded_file)
				if pdf_text and len(pdf_text.strip()) > 0:
					st.success("✅ PDF text extracted successfully!")
					# Use first 1000 chars as query (usually abstract/intro)
					pdf_query = " ".join(pdf_text.split())[:1000]
					st.info(f"Using first {len(pdf_query)} characters as search query")
				else:
					st.warning("⚠️ Could not extract text from PDF. Try entering a manual query.")
			except Exception as e:
				st.error(f"❌ Error extracting PDF: {str(e)}")

		# Determine final query
		final_query = query if query else pdf_query

		# Auto-search when the query changes or when Search button is clicked
		should_search = False
		if search_button:
			should_search = True
		elif final_query and st.session_state.last_query != final_query:
			# run automatic search when user enters a new query (convenience)
			should_search = True

		if should_search:
			if not final_query:
				st.error("❌ Please enter a query or upload a PDF with extractable text.")
			else:
				with st.spinner("🔄 Searching through papers..."):
					try:
						kws = [k.strip() for k in keywords.split(",")] if keywords else None
						results = search_index(
							final_query,
							DEFAULT_INDEX,
							DEFAULT_META,
							model_name=model_name,
							top_k=top_k,
							year_range=year_range,
							keywords=kws,
							rerank=rerank,
						)
						st.session_state.search_results = results
						st.session_state.last_query = final_query
					except Exception as e:
						st.error(f"❌ Search error: {str(e)}")
						st.session_state.search_results = None

	# Display results
	st.markdown("---")
	if st.session_state.search_results is not None:
		results = st.session_state.search_results
		if len(results) == 0:
			st.warning(f"⚠️ No results found for: '{st.session_state.last_query}' with current filters.")
		else:
			st.markdown(f"### 📊 Found {len(results)} results for: *{st.session_state.last_query[:80]}...*")
			
			for idx, r in enumerate(results, 1):
				with st.container():
					st.markdown(f"**{idx}. {r.get('title', 'Untitled')}**")
					
					col1, col2, col3 = st.columns([2, 1, 1])
					with col1:
						st.write(f"👥 **Authors:** {r.get('authors', 'Unknown')}")
						st.write(f"📅 **Year:** {r.get('year', 'N/A')}")
					with col2:
						score = r.get('rerank_score', r.get('score', 0))
						st.markdown(f'<p class="similarity-score">⭐ {score:.4f}</p>', unsafe_allow_html=True)
					with col3:
						if r.get("pdf_link"):
							st.markdown(f"[📥 PDF]({r.get('pdf_link')})")
					
					abstract = r.get("abstract", "")
					if abstract:
						st.write(f"**Abstract:** {abstract[:500]}{'...' if len(abstract) > 500 else ''}")
					
					st.markdown("---")


if __name__ == "__main__":
	run_app()

