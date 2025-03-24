import streamlit as st
from langchain_openai import ChatOpenAI, OpenAIEmbeddings

# Build kwargs for the LLM and Embeddings models
llm_kwargs = {
    "openai_api_key": st.secrets["OPENAI_API_KEY"],
    "model": st.secrets["OPENAI_MODEL"],
}
embeddings_kwargs = {
    "openai_api_key": st.secrets["OPENAI_API_KEY"],
    "model": 'text-embedding-3-small'
}

# Add base_url if it exists in the secrets
if "OPENAI_BASE_URL" in st.secrets:
    llm_kwargs["base_url"] = st.secrets["OPENAI_BASE_URL"]
    embeddings_kwargs["base_url"] = st.secrets["OPENAI_BASE_URL"]

# Initialize the LLM and Embedding Model with the conditional arguments
llm = ChatOpenAI(**llm_kwargs)
embeddings = OpenAIEmbeddings(**embeddings_kwargs)
