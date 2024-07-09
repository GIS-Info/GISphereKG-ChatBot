import sys
import os
# sys.path.append(os.path.dirname(os.getcwd()))
# from langchain.vectorstores.neo4j_vector import Neo4jVector
# from langchain.embeddings import OpenAIEmbeddings
from langchain_community.embeddings import OpenAIEmbeddings
from langchain_community.vectorstores import Neo4jVector
from constants import OPENAI_API_KEY, NEO4J_URL, NEO4J_USERNAME, NEO4J_PASSWORD


os.environ['OPENAI_API_KEY'] = OPENAI_API_KEY

"""
Embedding for the textual property of node (1536 length)
For the first time to do embedding

Only use this file for only one time, if there is no embedding for researchInterest
"""
# neo4j_db = Neo4jVector.from_existing_graph(
#     OpenAIEmbeddings(),
#     url = NEO4J_URL,
#     username=NEO4J_USERNAME,
#     password=NEO4J_PASSWORD,
#     node_label= 'ResearchInterest',
#     embedding_node_property="embedding",
#     text_node_properties=["research_interest"],
#     index_name="ri_embedding"
# )

"""
Use Embeddings from the existing index
"""
# neo4j_store = Neo4jVector.from_existing_index(
#     OpenAIEmbeddings(),
#     url = NEO4J_URL,
#     username=NEO4J_USERNAME,
#     password=NEO4J_PASSWORD,
#     database="neo4j",
#     index_name = 'ri_embedding',
#     embedding_node_property = "embedding",
#     text_node_property = "research_interest"
# )
# result = neo4j_store.similarity_search("map visualization", k = 2)
# print(result)