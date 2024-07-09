import streamlit as st
from langchain_openai import ChatOpenAI, OpenAIEmbeddings

openai_api_key = st.secrets['OPENAI_API_KEY']
openai_model = st.secrets['OPENAI_MODEL']

# Create the LLM
llm = ChatOpenAI(
    openai_api_key = st.secrets['OPENAI_API_KEY'],
    model = st.secrets['OPENAI_MODEL']
)

# Create the Embedding model
embeddings = OpenAIEmbeddings(
    openai_api_key = st.secrets['OPENAI_API_KEY']
)