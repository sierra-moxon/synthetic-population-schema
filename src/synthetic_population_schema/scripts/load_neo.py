import os
import glob
from neo4j import GraphDatabase


# Define the Neo4j loader class
class Neo4jLoader:
    def __init__(self, uri, user, password):
        self.driver = GraphDatabase.driver(uri, auth=(user, password))

    def close(self):
        self.driver.close()

    def load_file(self, file_path, class_name):
        with self.driver.session() as session:
            with open(file_path, "r") as f:
                headers = f.readline().strip().split("\t")  # Assuming TSV format
                for line in f:
                    values = line.strip().split("\t")
                    data = dict(zip(headers, values))
                    query = f"""
                    CREATE (n:{class_name} {{ {', '.join([f'{k}: $data.{k}' for k in headers])} }})
                    """
                    session.run(query, data=data)


# Main loader function
def load_all_data(directory, uri="bolt://localhost:7687", user="neo4j", password="test123"):
    loader = Neo4jLoader(uri, user, password)
    try:
        subdirectories = [d for d in glob.glob(os.path.join(directory, "*")) if os.path.isdir(d)]
        for subdir in subdirectories:
            for file_path in glob.glob(os.path.join(subdir, "*.txt")):
                class_name = os.path.basename(file_path).split("_")[2]  # Derive class from filename
                loader.load_file(file_path, class_name)
    finally:
        loader.close()


def download_data():
    # Download the data from the web
    pass



if __name__ == "__main__":
    base_dir = "path/to/your/data"  # Replace with the root directory of your TSV files
    load_all_data(base_dir)