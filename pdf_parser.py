import os

# Docling runs its layout model through torch.compile() by default.
# torch.compile's inductor backend needs a C++ compiler (cl.exe) on PATH,
# which is not available from a normal shell on Windows. 
os.environ.setdefault("DOCLING_INFERENCE_COMPILE_TORCH_MODELS", "false")

from pathlib import Path

from docling.document_converter import DocumentConverter

source_dir = Path(__file__).resolve().parent
source = source_dir / "samples" / "RAG.pdf"

converter = DocumentConverter()
doc = converter.convert(source).document

# Save parsed file as markdown
markdown = doc.export_to_markdown()

output = Path("parsed_document.md")
output.write_text(markdown, encoding="utf-8")

print(f"Saved parsed document to: {output.resolve()}")
