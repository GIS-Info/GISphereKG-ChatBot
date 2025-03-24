import streamlit as st
import sys
from langchain.chains import GraphCypherQAChain

sys.path.append("../")
from llm import llm
from graph import graph


# Create the Cypher QA chain
cypher_qa = GraphCypherQAChain.from_llm(
    llm,
    graph = graph,
    allow_dangerous_requests = True
)

