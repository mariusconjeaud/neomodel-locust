# neomodel-locust
Performance tests for neomodel

## How to use
It's based on locust, so in order to run it, run the following commands :

```python
# Start the test API
# Note that it's tied to a branch for the neomodel repo
pipenv install
pipenv run start

# In a separate terminal
pipenv run locust
```

Then, go to the Locust UI, and pass the following parameters (adjust accordingly):

|Parameter|Value (default)|
|---|---|
|Number of users|1|
|Ramp up|1|
|Host|http://localhost:8000|
|Run time (advanced)|10|

## Results

### neomodel overhead vs Neo4j driver

For this test, we compared pushing a Cypher query through :

* Neo4j driver low-level `session.run`
* neomodel `db.cypher_query`(which wraps `session.run`)
* Neo4j driver high-level `driver.execute_query`

The results show that neomodel adds very little overhead to the Neo4j driver.

Results :

![Results table](/img/neomodel_overhead.png "Results table")

### Sync vs Async comparison

For this test, we compared sync neomodel vs async neomodel, in two ways :

* Serial queries - Async should not provide a boost here since we wait for each query before going to the next ; but also should not too much overhead
* Concurrent queries - We make use of `asyncio.gather` for async, and create a `thread pool` for sync so that queries happen concurrently. Here, async should be more performant than sync

Results :

![Results table](/img/sync_async_comparison.png "Results table")
