from locust import HttpUser, task


class Neo4jUser(HttpUser):
    @task
    def perform_serial_queries_sync(self):
        self.client.get("/serial_sync_queries")

    @task
    def perform_serial_queries_async(self):
        self.client.get("/serial_async_queries")

    @task
    def perform_concurrent_queries_sync(self):
        self.client.get("/concurrent_sync_queries")

    @task
    def perform_concurrent_queries_async(self):
        self.client.get("/concurrent_async_queries")

    # @task
    # def perform_neomodel_query(self):
    #     self.client.get("/neomodel_query")

    # @task
    # def perform_driver_execute_query(self):
    #     self.client.get("/driver_execute_query")

    # @task
    # def perform_driver_session_query(self):
    #     self.client.get("/driver_session_query")
