import streamlit as st
import sys
from langchain.chains import GraphCypherQAChain

sys.path.append("../")
from graph import graph


def cypher_qa(llm):
    """Create GraphCypherQAChain with dynamic LLM"""
    return GraphCypherQAChain.from_llm(
        llm,
        graph=graph,
        allow_dangerous_requests=True
    )
