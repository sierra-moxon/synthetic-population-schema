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
        if file.endswith(".txt") and ("school" or "household") in file:
            if "school" in file:
                print(f"Loading schools...{file}")
                query = f"""
                    LOAD CSV WITH HEADERS FROM 'file:///2010/State/{file}' AS row
                    MERGE (s:School {{id: row.sp_id}})
                    SET s.name = row.name,
                        s.city = row.city,
                        s.county = row.county,
                        s.zipcode = row.zipcode,
                        s.total_students = toInteger(row.total),
                        s.latitude = toFloat(row.latitude),
                        s.longitude = toFloat(row.longitude);
                """
            execute_query(query)
            if "household" in file:
                print(f"Loading households...{file}")
                query = f"""
                    LOAD CSV WITH HEADERS FROM 'file:///2010/State/{file}' AS row
                    MERGE (h:Household {{id: row.sp_id}})
                    SET h.city = row.city,
                        h.county = row.county,
                        h.zipcode = row.zipcode,
                        h.latitude = toFloat(row.latitude),
                        h.longitude = toFloat(row.longitude);
                        """
            execute_query(query)
    driver.close()
    print("Data ingestion into Neo4j complete!")