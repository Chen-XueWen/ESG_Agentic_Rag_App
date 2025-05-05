from langchain.vectorstores import Chroma
from langchain.embeddings import SentenceTransformerEmbeddings

def get_relevant_context(query, persist_dir="chroma_db", k=5):
    vectordb = Chroma(persist_directory=persist_dir, embedding_function=SentenceTransformerEmbeddings(model_name="all-MiniLM-L6-v2"))
    retriever = vectordb.as_retriever(search_kwargs={"k": k})
    docs = retriever.get_relevant_documents(query)
    return "\n\n".join([doc.page_content for doc in docs])
