import requests

endpoint = 'http://localhost:8000/api/student-vouchers/'

data = {
    'code': 'ABC-DEF',
    'percentage': 5
}

# get_response = requests.get(endpoint)
get_response = requests.post(endpoint, json=data)
# print(get_response.json())
print(get_response.status_code) 
