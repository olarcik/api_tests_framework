import allure

class Endpoint:
    url = 'https://jsonplaceholder.typicode.com/posts'
    response = None
    json = None
    headers = {'Content-Type': 'application/json'}

    @allure.step('Check if created user`s title is correct')
    def check_response_is_correct(self, title):
        assert self.json['title'] == title, 'Title is incorrect'
