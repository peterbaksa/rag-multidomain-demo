from langchain_community.document_loaders import PyPDFLoader
from langchain.schema import Document
from pathlib import Path
from typing import List


def load_pdf_documents(pdf_path: str) -> List[Document]:
    """
    Loads a PDF file using PyPDFLoader and returns a list of Document objects.

    Args:
        pdf_path (str): Path to the PDF file.

    Returns:
        List[Document]: List of LangChain Document objects, one per page.
    """
    if not Path(pdf_path).is_file():
        raise FileNotFoundError(f"File not found: {pdf_path}")

    loader = PyPDFLoader(pdf_path)
    documents = loader.load()

    return documents
