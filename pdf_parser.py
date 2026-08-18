import os

# Docling runs its layout model through torch.compile() by default.
# torch.compile's inductor backend needs a C++ compiler (cl.exe) on PATH,
# which is not available from a normal shell on Windows. 
os.environ.setdefault("DOCLING_INFERENCE_COMPILE_TORCH_MODELS", "false")

from pathlib import Path

from docling.datamodel.base_models import InputFormat
from docling.datamodel.pipeline_options import (
    OcrMode,
    PdfPipelineOptions,
    TableStructureOptions,
    EasyOcrOptions,
)
from docling.datamodel.settings import DEFAULT_PAGE_RANGE
from docling.document_converter import DocumentConverter, PdfFormatOption

IS_CI = os.environ.get("CI","").lower() in ("true", "1", "yes")
CI_PAGE_RANGE = (1, 5)


source_dir = Path(__file__).resolve().parent
source = source_dir / "samples" / "RAG.pdf"


# Pipeline
pipeline_options = PdfPipelineOptions()
pipeline_options.do_ocr = True
pipeline_options.do_table_structure = True
pipeline_options.table_structure_options = TableStructureOptions(
    do_cell_matching=True
)

# OCR Options
ocr_options = EasyOcrOptions(mode=OcrMode.FULL_PAGE)
pipeline_options.ocr_options = ocr_options


converter = DocumentConverter(
    format_options={
        InputFormat.PDF: PdfFormatOption(
            pipeline_options=pipeline_options,
        )
    }
)

page_range = CI_PAGE_RANGE if IS_CI else DEFAULT_PAGE_RANGE
doc = converter.convert(source, page_range=page_range).document

# Save parsed file as markdown
markdown = doc.export_to_markdown()

output = Path("parsed_document_with_ocr.md")
output.write_text(markdown, encoding="utf-8")

print(f"Saved parsed document to: {output.resolve()}")
