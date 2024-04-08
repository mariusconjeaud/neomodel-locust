from locust import HttpUser, task


class Neo4jUser(HttpUser):
    @task
    def perform_queries_sync(self):
        self.client.get("/sync_queries")

    @task
    def perform_queries_async(self):
        self.client.get("/async_queries")

    @task
    def perform_neomodel_query(self):
        self.client.get("/neomodel_query")

    @task
    def perform_driver_query(self):
        self.client.get("/driver_query")
