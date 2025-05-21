from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.schema import Document
from typing import List


def split_documents(
    documents: List[Document],
    chunk_size: int = 500,
    chunk_overlap: int = 100
) -> List[Document]:
    """
    Splits a list of LangChain Document objects into smaller chunks.

    Args:
        documents (List[Document]): Input documents.
        chunk_size (int): Target size of each chunk in characters.
        chunk_overlap (int): Overlap between chunks to preserve context.

    Returns:
        List[Document]: List of chunked Document objects.
    """
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=chunk_size,
        chunk_overlap=chunk_overlap,
        separators=["\n\n", "\n", " ", ""],
    )

    chunked_docs = splitter.split_documents(documents)
    return chunked_docs
