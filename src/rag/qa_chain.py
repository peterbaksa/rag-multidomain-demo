from langchain.chains import RetrievalQA
from langchain.vectorstores.base import VectorStoreRetriever
from langchain_openai import ChatOpenAI


def create_qa_chain(retriever: VectorStoreRetriever) -> RetrievalQA:
    """
    Creates a RetrievalQA chain with a retriever and OpenAI LLM.
    On each query, the chain uses the retriever to fetch relevant chunks
    and then passes them along with the question to the LLM.

    "stuff" – inserts all documents at once (works for short inputs)
    "map_reduce" – answers each chunk separately and then summarizes it
    "refine" – answers 1 chunk and the others just refine the answer

    Args:
        retriever (VectorStoreRetriever): A retriever object from vectorstore.

    Returns:
        RetrievalQA: Configured QA chain ready for .run(question)
    """
    llm = ChatOpenAI(temperature=0)
    qa_chain = RetrievalQA.from_chain_type(
        llm=llm,
        chain_type="stuff",  # default behavior: stuff all docs into prompt
        retriever=retriever,
        return_source_documents=False
    )
    return qa_chain
