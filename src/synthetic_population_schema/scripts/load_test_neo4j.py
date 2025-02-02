from neo4j import GraphDatabase


if __name__ == "__main__":
    uri = "bolt://localhost:7687"
    user = "neo4j"
    password = "synthpop_123"

    query = """
LOAD CSV WITH HEADERS FROM 'file:///2010/State/2010_ver1_56_pums_p.txt' AS row
RETURN row.serialno, row.st, row.agep
LIMIT 5;
    """

    driver = GraphDatabase.driver(uri, auth=(user, password))

    with driver.session() as session:
        result = session.run(query)
        for record in result:
            print(record)