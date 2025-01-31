from neo4j import GraphDatabase

class Neo4jLoader:
    def __init__(self, uri, user, password):
        self.driver = GraphDatabase.driver(uri, auth=(user, password))

    def close(self):
        self.driver.close()

    def load_file(self, file_path, class_name):
        """
        Load a single .txt file into Neo4j as nodes.
        """
        print(f"Loading {file_path} into Neo4j as {class_name}...")
        with self.driver.session() as session:
            with open(file_path, "r") as file:
                headers = file.readline().strip().split("\t")  # Assuming TSV format
                for line in file:
                    values = line.strip().split("\t")
                    data = dict(zip(headers, values))
                    query = f"""
                    CREATE (n:{class_name} {{ {', '.join([f'{k}: $data.{k}' for k in headers])} }})
                    """
                    session.run(query, data=data)
        print(f"Completed loading {file_path}.")





def main():
    # Directory paths
    zip_dir = "/Users/SMoxon/.data/synthetic_populations/2010/State"
    extract_to = "/Users/SMoxon/.data/synthetic_populations/extracted"

    # Neo4j credentials
    neo4j_uri = "bolt://localhost:7687"
    neo4j_user = "neo4j"
    neo4j_password = "test123"

    # Create Neo4jLoader instance
    loader = Neo4jLoader(neo4j_uri, neo4j_user, neo4j_password)

    try:
        unzip_and_process(zip_dir, extract_to, loader)
    finally:
        loader.close()


if __name__ == "__main__":
    main()
