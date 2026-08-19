from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnablePassthrough
from langchain_core.output_parsers import StrOutputParser
from langchain_groq import ChatGroq
from vector import vector_store


prompt = ChatPromptTemplate.from_template("""
Use the following pieces of context to answer the question at the end.
If you don't know the answer, say that you don't know.
Context: {context}
Question: {question}
""")

llm = ChatGroq(
    model="openai/gpt-oss-20b",
    temperature=0
)

retriever = vector_store.as_retriever(
    search_type="similarity",
    search_kwargs={"k": 2}
)


# LCEL Retrieval Chain
chain = (
    {"context": retriever, "question": RunnablePassthrough()}
    | prompt
    | llm
    | StrOutputParser()
)