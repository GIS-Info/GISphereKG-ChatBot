import sys
from langchain_community.vectorstores import Neo4jVector
import streamlit as st

sys.path.append("../")
from llm import get_embeddings

if __name__ == "__main__":
    """
    Embedding for the textual property of node
    For the first time to do embedding

    Only use this file for only one time, if there is no embedding for researchInterest
    """

    embeddings_instance = get_embeddings(
        st.secrets['OPENAI_API_KEY'],
        st.secrets['OPENAI_BASE_URL']
    )

    neo4j_db = Neo4jVector.from_existing_graph(
        embedding=embeddings_instance,
        url = st.secrets['NEO4J_URI'],
        username = st.secrets['NEO4J_USERNAME'],
        password = st.secrets['NEO4J_PASSWORD'],
        node_label = 'ResearchInterest',
        embedding_node_property = "embedding",
        text_node_properties = ["research_interest"],
        index_name = "ri_embedding"
    )
    print('Neo4jVector created')

    """
    Use Embeddings from the existing index
    """
    neo4j_store = Neo4jVector.from_existing_index(
        embedding=embeddings_instance,
        url = st.secrets['NEO4J_URI'],
        username = st.secrets['NEO4J_USERNAME'],
        password = st.secrets['NEO4J_PASSWORD'],
        database="neo4j",
        index_name = 'ri_embedding',
        embedding_node_property = "embedding",
        text_node_property = "research_interest",
    )
    result = neo4j_store.similarity_search("map visualization", k = 2)
    print(result)