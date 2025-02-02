from neo4j import GraphDatabase

if __name__ == "__main__":
    uri = "bolt://localhost:7687"
    user = "neo4j"
    password = "synthpop_123"
    driver = GraphDatabase.driver(uri, auth=(user, password))

    query = """
        LOAD CSV WITH HEADERS FROM 'file:///2010/State/2010_ver1_19_schools.txt' AS row
        MERGE (s:School {id: row.sp_id})
        SET s.name = row.name,
            s.city = row.city,
            s.county = row.county,
            s.zipcode = row.zipcode,
            s.total_students = toInteger(row.total),
            s.latitude = toFloat(row.latitude),
            s.longitude = toFloat(row.longitude);
    """

    with driver.session() as session:
        result = session.run(query)
        for record in result:
            print(record["row"], " | Keys:", record["keys(row)"])

    driver.close()
