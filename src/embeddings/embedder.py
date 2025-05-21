from langchain_openai.embeddings import OpenAIEmbeddings

def get_openai_embedder(api_key: str) -> OpenAIEmbeddings:
    """
    Initializes and returns an embedding model instance.

    Args:
        api_key (str): OPENAI_API_KEY

    Returns:
        An instance of LangChain-compatible embedding model.
    """
    return OpenAIEmbeddings(openai_api_key=api_key)
