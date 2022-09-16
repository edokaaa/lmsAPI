import requests
from login import get_token, api_url

token = get_token()

if token is not None:

    headers = {
        'Authorization': f'Bearer {token}'
    }

    response = requests.get(f'{api_url}lms/courses/', headers=headers)

    print(response.json())
    print(response.status_code)
    
else:
    print('Unsuccessful')
