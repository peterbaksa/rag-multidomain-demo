from langchain_community.vectorstores import FAISS
from langchain.schema import Document
from langchain.embeddings.base import Embeddings
from typing import List


def create_faiss_vectorstore(
    documents: List[Document],
    embedder: Embeddings
) -> FAISS:
    """
    Creates a new FAISS vector store from the provided documents.
    The index is created fresh on every run (no persistence).

    Args:
        documents (List[Document]): Chunked documents to index.
        embedder (Embeddings): The embedding model used to generate vectors.

    Returns:
        FAISS: An in-memory FAISS vector store instance.
    """
    vectorstore = FAISS.from_documents(documents, embedder)
    return vectorstore
