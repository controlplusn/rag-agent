from langchain_text_splitters import RecursiveCharacterTextSplitter

from document_loader import documents

splitter = RecursiveCharacterTextSplitter(
    separators=["\n\n", "\n", " ", ""],
    chunk_size=100,
    chunk_overlap=10
)

chunks = splitter.split_documents(documents)

# print(chunks)
# print([len(chunk.page_content) for chunk in chunks])