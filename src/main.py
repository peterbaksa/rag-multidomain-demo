import os
from dotenv import load_dotenv
from src.loaders.pdf_loader import load_pdf_documents
from src.preprocessing.splitter import split_documents
from src.embeddings.embedder import get_openai_embedder
from src.vectorstore.faiss_store import create_faiss_vectorstore
from src.rag.qa_chain import create_qa_chain
from pathlib import Path


load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

# === Step 1: Load PDF file ===
# Set path to the root of the project. Works in both: python main.py AND interactive console
if '__file__' in globals():
    ROOT_DIR = Path(__file__).resolve().parent.parent
else:
    ROOT_DIR = Path.cwd()
pdf_path = ROOT_DIR / "data" / "python_programming.pdf"
documents = load_pdf_documents(pdf_path)
print(f"[INFO] Loaded {len(documents)} pages from PDF.")

# === Step 2: Split into chunks ===
chunked_docs = split_documents(documents)
print(f"[INFO] Split into {len(chunked_docs)} chunks.")

# === Step 3: Get embedding model ===
embedder = get_openai_embedder(OPENAI_API_KEY)
print(f"[INFO] Embedding model initialized.")

# === Step 4: Create FAISS vectorstore ===
vectorstore = create_faiss_vectorstore(chunked_docs, embedder)
retriever = vectorstore.as_retriever()
print(f"[INFO] Vector store created and ready.")

# === Step 5: Create QA chain ===
qa_chain = create_qa_chain(retriever)
print(f"[INFO] QA chain is ready.")

# === Step 6: Ask a test question ===
question = "What is a function in Python?"
answer = qa_chain.invoke(question)

# === Step 7: Output answer ===
print("\n--- Question & Answer ---")
print(f"Q: {question}")
print(f"A: {answer.get('result', 'No answer found.')}")
