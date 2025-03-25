from langchain_openai import ChatOpenAI, OpenAIEmbeddings

def get_llm(api_key, model, base_url=None):
    """Create ChatOpenAI instance with dynamic credentials"""
    llm_kwargs = {
        "openai_api_key": api_key,
        "model": model,
    }
    if base_url:
        llm_kwargs["base_url"] = base_url
    return ChatOpenAI(**llm_kwargs)

def get_embeddings(api_key, base_url=None):
    """Create OpenAIEmbeddings instance with dynamic credentials"""
    embeddings_kwargs = {
        "openai_api_key": api_key,
        "model": 'text-embedding-3-small'
    }
    if base_url:
        embeddings_kwargs["base_url"] = base_url
    return OpenAIEmbeddings(**embeddings_kwargs)