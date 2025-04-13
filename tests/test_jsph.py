import pytest

TEST_DATA = [
    { "title": "foor", "body": "bars", "userId": 134},
    { "title": "poor", "body": "bars", "userId": 135},
    { "title": "door", "body": "bars", "userId": 136}
]

@pytest.mark.parametrize('data', TEST_DATA)
def test_post_a_post(create_post_endpoint, data):
    create_post_endpoint.create_new_post(payload=data)
    create_post_endpoint.check_response_status_is_200()
    create_post_endpoint.check_response_is_correct(data['title'])

def test_update_a_post(update_post_endpoint):
    payload = {
        "title": "My titleUPD",
        "body": "my bodyUPD",
        "userId": 2
    }
    update_post_endpoint.make_changes_in_post(42, payload)
    update_post_endpoint.check_response_status_is_200()
    update_post_endpoint.check_response_is_correct(payload['title'])