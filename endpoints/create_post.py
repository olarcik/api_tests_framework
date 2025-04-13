from endpoints.endpoint import Endpoint
import requests
import allure

class CreatePost(Endpoint):

    @allure.step('Create new post')
    def create_new_post(self, payload, headers=None):
        if len(payload['body']) > 1000:
            self.url = f'{self.url}/dlinopost'
        headers = headers if headers else self.headers
        self.response = requests.post(
            self.url,
            json=payload,
            headers=headers
        )
        self.json = self.response.json()
        return self.response

    @allure.step('Check that response is 200')
    def check_response_status_is_200(self):
        assert  self.response.status_code == 201
