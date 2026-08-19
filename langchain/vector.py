from langchain_chroma import Chroma 

from text_splitting import chunks
from embedding import embedding_model

vector_store = Chroma(
    collection_name="rag_collection",
    embedding_function=embedding_model
)


vector_store.add_documents(chunks)