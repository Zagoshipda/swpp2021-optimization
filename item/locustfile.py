from locust import HttpUser, between, task

class Websiteuser(HttpUser):
    wait_time = between(3, 8)

    @task
    def my_task(self):
        self.client.get('/')
