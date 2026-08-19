from pathlib import Path
from langchain_community.document_loaders import PyPDFLoader

source_dir = Path(__file__).resolve().parent.parent
source_doc = source_dir / "samples" / "RAG.pdf"

pdf_loader = PyPDFLoader(source_doc)
documents = pdf_loader.load()