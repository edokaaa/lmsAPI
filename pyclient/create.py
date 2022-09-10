import requests
# from .defaults import api_url
api_url = 'http://localhost:8000/'

def create_course():

    endpoint = f'{api_url}lms/courses/'

    data = {
        "name": "test2",
        "description": "test2",
        "duration": 2,
        "tutor": 1
    }

    # get_response = requests.get(endpoint)
    get_response = requests.post(endpoint, json=data)
    print(get_response.status_code) 
    # print(get_response.json())

create_course()