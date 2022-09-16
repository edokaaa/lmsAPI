from json import JSONDecodeError
import requests
from login import get_token, api_url

token = get_token()

if token is not None:

    headers = {
        'Authorization': f'Bearer {token}'
    }

    data = {
        "name": "test",
        "description": "demo",
        "duration": 3,
        "tutor": 1,
        "price": 200,
        "track": 1
    }
    
    response = requests.post(f'{api_url}lms/courses/', headers=headers, json=data)
    try:
        print(response.json())
    except JSONDecodeError:
        print('unable to decode json')
    print(response.status_code)
    
else:
    print('Unsuccessful')
