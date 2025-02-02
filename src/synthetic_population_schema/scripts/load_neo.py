import os
from neo4j import GraphDatabase


NEO4J_URI = "bolt://localhost:7687"  # Change if needed
NEO4J_USER = "neo4j"
NEO4J_PASSWORD = "synthpop_123"  # Change if needed


def load_data_into_neo4j(state_dir):
    """
    Loads the parsed CSV data into Neo4j using LOAD CSV for bulk inserts.
    """
    driver = GraphDatabase.driver(NEO4J_URI, auth=(NEO4J_USER, NEO4J_PASSWORD))

    def execute_query(query, parameters=None):
        with driver.session() as session:
            session.run(query, parameters)

    for file in os.listdir(state_dir):
        if file.endswith(".txt"):
            file_path = f"/var/lib/neo4j/import/2010/State/{file}"
            parts = file.split("_")

            print(f"Ingesting {file} into Neo4j...")

            #     LOAD CSV FROM 'file:///2010/State/2010_ver1_56_pums_p.txt' AS row
            print(f"Loading {file_path} into Neo4j...")
            query = f"""
            LOAD CSV WITH HEADERS FROM 'file://{file_path}' AS row
            """

            print(query)
            execute_query(query)

    driver.close()
    print("Data ingestion into Neo4j complete!")