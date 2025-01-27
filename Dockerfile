# Dockerfile
FROM neo4j:5.10

# Set environment variables for Neo4j
ENV NEO4J_AUTH=neo4j/test123
ENV NEO4J_dbms_default__listen__address=0.0.0.0

# Expose Neo4j ports
EXPOSE 7474 7687