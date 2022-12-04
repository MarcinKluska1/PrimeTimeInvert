from locust import FastHttpUser, task, User
import random


class QuickstartUser(FastHttpUser):
    host = 'https://primeinvertauth.herokuapp.com'

    @task
    def get_time_test(self):
        self.client.get('/get-time/', auth=('user', 'password'))

    @task
    def picture_inversion_test(self):
        with open('test.jpg', 'rb') as image:
            self.client.post(
                '/picture-inversion/',
                files={'file': image}
            )

    @task
    def prime_number_test(self):
        number = str(random.randint(10 ** 10, 10 ** 14))
        self.client.get(
            '/prime-test/' + number,
            name="/prime-test/random_number"
        )
