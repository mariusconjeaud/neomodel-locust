from contextlib import asynccontextmanager
from fastapi import FastAPI
from neomodel import db, adb
from neomodel import config
from neo4j import GraphDatabase


QUERIES = [
    "MATCH (n) WHERE n.name='Person_25153' RETURN n",
    "MATCH (n) WHERE n.name='Dog_48672' RETURN n",
    "MATCH (n) WHERE n.name='Person_654' RETURN n",
    "MATCH (n) WHERE n.name='Dog_89774' RETURN n",
    "MATCH (n) WHERE n.name='Person_96845' RETURN n",
    "MATCH (n) WHERE n.name='Dog_9864' RETURN n",
    "MATCH (n) WHERE n.name='Person_1' RETURN n",
    "MATCH (n) WHERE n.name='Dog_2' RETURN n",
]
DRIVER = None


async def startup_event():
    config.DATABASE_URL = "bolt://neo4j:foobarbaz@localhost:7687/locust"

    global DRIVER
    DRIVER = GraphDatabase.driver("bolt://localhost:7687", auth=("neo4j", "foobarbaz"))

    results, _ = db.cypher_query("MATCH (n) RETURN count(n) > 0")
    if results[0][0] is False:
        db.cypher_query(
            """
                UNWIND range(0, 1000000) AS counter
                CALL {
                    WITH counter
                    CREATE (p:Person {name: 'Person_' + counter})
                    CREATE (d:Dog {name: 'Dog_' + counter})
                } IN TRANSACTIONS OF 10000 ROWS
            """
        )


@asynccontextmanager
async def lifespan(app: FastAPI):
    """
    This function is called on application startup.
    """
    await startup_event()
    yield


app = FastAPI(lifespan=lifespan)


@app.get("/sync_queries")
def run_sync_queries():
    results = []
    for query in QUERIES:
        result, _ = db.cypher_query(query)
        results.append(result)
    return results


@app.get("/async_queries")
async def run_async_queries():
    results = []
    for query in QUERIES:
        result, _ = await adb.cypher_query(query)
        results.append(result)
    return results


@app.get("/neomodel_query")
def run_neomodel_query():
    records, meta = db.cypher_query("MATCH (n) RETURN count(n)")
    return records


@app.get("/driver_query")
def run_driver_query():
    records, summary, keys = DRIVER.execute_query("MATCH (n) RETURN count(n)")
    return records
