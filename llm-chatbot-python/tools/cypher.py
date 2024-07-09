import streamlit as st
from llm import llm
from graph import graph
import sys

sys.path.append("../")
# Create the Cypher QA chain
from langchain.chains import GraphCypherQAChain
from llm import llm
from graph import graph

cypher_qa = GraphCypherQAChain.from_llm(
    llm,
    graph = graph
)

