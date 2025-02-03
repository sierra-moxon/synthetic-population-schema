import os
from neo4j import GraphDatabase


NEO4J_URI = "bolt://localhost:7687"  # Change if needed
NEO4J_USER = "neo4j"
NEO4J_PASSWORD = "synthpop_123"  # Change if needed

driver = GraphDatabase.driver(NEO4J_URI, auth=(NEO4J_USER, NEO4J_PASSWORD))

def execute_query(query, parameters=None):
    with driver.session() as session:
        session.run(query, parameters)

def reset_database():
    """Drops all nodes, relationships, and indexes before reloading data."""
    queries = [
        "MATCH (n) DETACH DELETE n;",  # Deletes all nodes and relationships
        "CALL apoc.schema.assert({}, {});"  # Drops all indexes and constraints (requires APOC plugin)
    ]
    with driver.session() as session:
        for query in queries:
            session.run(query)
            print(f"Executed: {query}")

def create_indexes():
    indexes = [
        "CREATE INDEX household_id_index FOR (h:Household) ON (h.id)",
        "CREATE INDEX person_id_index FOR (p:Person) ON (p.id)",
        "CREATE INDEX workplace_id_index FOR (w:Workplace) ON (w.id)",
        "CREATE INDEX school_id_index FOR (s:School) ON (s.id)"
    ]

    with driver.session() as session:
        for index_query in indexes:
            session.run(index_query)
            print(f"Executed: {index_query}")

def load_data_into_neo4j(state_dir):
    """
    Loads the parsed CSV data into Neo4j using LOAD CSV for bulk inserts.
    """

    reset_database()
    create_indexes()
    for file in os.listdir(state_dir):
        if (file.endswith(".txt")
                and ("school" or "household" or "workplaces" or "2010_ver1_33_synth_people" in file)
                and "33" in file
                and "gq" not in file):
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
            if "workplaces" in file:
                """
                sp_id,workers,latitude,longitude
                506961021,11,43.1410324,-95.1442630
                506675820,1,42.1989823,-91.6638940
                506888583,11,42.4991242,-90.6820073
                """
                print(f"Loading workplaces...{file}")
                query = f"""
                    LOAD CSV WITH HEADERS FROM 'file:///2010/State/{file}' AS row
                    MERGE (w:Workplace {{id: row.sp_id}})
                    SET w.workers = toInteger(row.workers),
                        w.latitude = toFloat(row.latitude),
                        w.longitude = toFloat(row.longitude);
                        """
                execute_query(query)
            if "people" in file:
                """
                    sp_id,sp_hh_id,serialno,stcotrbg,age,sex,race,sporder,relate,sp_school_id,sp_work_id
                    164084386,104704790,2007000946236,"190674805002",63,1,1,2,1,,506973539
                    164084388,104710516,2007000946236,"190693603003",63,1,1,2,1,,506909065
                    164085797,105163287,2007000946270,"191712904002",42,1,3,1,0,,506598530
                """
                print(f"Loading people...{file}")
                query = f"""
                    LOAD CSV WITH HEADERS FROM 'file:///2010/State/{file}' AS row
                    MERGE (ps:Person {{id: row.sp_id}})
                    SET ps.age = toInteger(row.age)
                    SET ps.sex = toInteger(row.sex)
                    SET ps.race = toInteger(row.race)
                    SET ps.sp_hh_id = row.sp_hh_id
                    SET ps.sp_school_id = row.sp_school_id
                    """
                execute_query(query)
    driver.close()
    print("Data ingestion into Neo4j complete!")