""" For better demonstrate use CONSOLE instead of TERMINAL run  """


'----- Document Loader -----'
from src.loaders.pdf_loader import load_pdf_documents
documents = load_pdf_documents("data/python_programming.pdf")
print(f"Loaded {len(documents)} documents.")
print(documents[40].page_content[:500])


'''----- Splitter -----'''
from src.preprocessing.splitter import split_documents
chunked_docs = split_documents(documents)
print(f"Number of chunks: {len(chunked_docs)}")
print(chunked_docs[40].page_content[:300])


'''----- Embedding -----'''
import os
from dotenv import load_dotenv
load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
from src.embeddings.embedder import get_openai_embedder
embedder = get_openai_embedder(OPENAI_API_KEY)
embedded_query = embedder.embed_query("This is an example query")
print(f"Embedding of query: {embedded_query}")


'''----- Vector Store -----'''
from src.vectorstore.faiss_store import create_faiss_vectorstore
vectorstore = create_faiss_vectorstore(documents=chunked_docs, embedder=embedder)
retriever = vectorstore.as_retriever()
retriever_invoke_response = retriever.invoke("What is python class")
print("Invoke retriever with text query return list of 4 most similar documents:")
print(*[f"Document #{idx}:\n {doc.page_content}\n\n" for idx, doc in enumerate(retriever_invoke_response)], sep='\n')


'''----- QA Chain -----'''
from src.rag.qa_chain import create_qa_chain
qa_chain = create_qa_chain(retriever)
question = "What is a function in Python?"
answer = qa_chain.invoke(question)
print(f"Q: {question}")
print(f"A: {answer.get('result', 'No answer found.')}")
