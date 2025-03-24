import os
import sys
import pandas as pd
from neo4j import GraphDatabase
from constants import NEO4J_URI, NEO4J_USERNAME, NEO4J_PASSWORD

threshold = 0.9
prof_sim_df = pd.read_csv(os.path.dirname(os.getcwd()) + "/data/prof_sim.csv")
scores = prof_sim_df['score'].tolist()
score_above = [s for s in scores if s > threshold]

# print(len(score_above), len(scores))

url = NEO4J_URI
auth = (NEO4J_USERNAME, NEO4J_PASSWORD)

with GraphDatabase.driver(url, auth = auth) as driver:
    driver.verify_connectivity()
    for index, row in prof_sim_df.iterrows():
        prof1 = row['prof1']
        prof2 = row['prof2']
        score = row['score']
        print(index, prof1, prof2, score)
        if prof1 != prof2:
            # cypher_statement = ,
            if score > threshold:
                r = driver.execute_query(
                    "match (p1:People{PersonID:'" + str(int(prof1)) + "'}), (p2:People{PersonID:'" + str(int(prof2)) +"'}) create (p1)-[r:isSimilarTo{score:" + str(score) + "}]->(p2) return r",
                    database = "neo4j"
                )
                print(r)
#


