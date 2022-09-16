import requests
from getpass import getpass # using this method to get password with echo off.


api_url = 'http://localhost:8000/'

def get_token():
    auth_endpoint = f'{api_url}auth/'

    username = input('Enter username: \n')
    password = getpass('Enter password: \n')

    data = {
        'username': username,
        'password': password
    }

    auth_response = requests.post(auth_endpoint, json=data)

    if auth_response.status_code == 200:
        print('Login Successful')
        # endpoint = f'{api_url}lms/courses/'

        token = auth_response.json()['token']

        return token
    return 'not ok'

if __name__ == '__main__':
    token = get_token()
    print(token)