from endpoints.endpoint import Endpoint
import requests
import allure

class UpdatePost(Endpoint):

    @allure.step('Update a post')
    def make_changes_in_post(self, post_id, payload, headers=None):
        headers = headers if headers else self.headers
        self.response = requests.put(
            f'{self.url}/{post_id}',
            json=payload,
            headers=headers
        )
        self.json = self.response.json()
        return self.response

    @allure.step('Check that response is 200')
    def check_response_status_is_200(self):
        assert self.response.status_code == 200

