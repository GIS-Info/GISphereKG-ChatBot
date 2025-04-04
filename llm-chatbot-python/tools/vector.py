import streamlit as st
from langchain_community.vectorstores import Neo4jVector
from langchain.chains import RetrievalQA, RetrievalQAWithSourcesChain

def kg_qa(llm, embeddings):
    """Create RetrievalQA with dynamic LLM and embeddings"""
    neo4jvector = Neo4jVector.from_existing_index(
        embeddings,
        url=st.secrets['NEO4J_URI'],
        username=st.secrets['NEO4J_USERNAME'],
        password=st.secrets['NEO4J_PASSWORD'],
        index_name='ri_embedding',
        node_label='ResearchInterest',
        text_node_property='research_interest',
        embedding_node_property='embedding',
        retrieval_query="""
            RETURN
            node.research_interest AS text,
            score,
            {
                researchInterest: node.research_interest,
                professor: [(people)-[:hasResearchInterestOf]->(node) | people.NAME_EN]
            } AS metadata
            """
    )
    return RetrievalQA.from_llm(
        llm=llm,
        retriever=neo4jvector.as_retriever(),
        verbose=True,
        return_source_documents=True
    )
