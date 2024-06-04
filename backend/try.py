import requests

url = 'http://127.0.0.1:5000/delete-content/users'
headers = {
    'x-access-token': 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJSRVBBMDAwNiIsImlhdCI6MTcxNzQ5NTE2NiwiZXhwIjoxNzE3NTgxNTY2fQ.8_BM0XkgK808K5sUlIwtDyDBFGSCXZlz7IUKiqn-LE8'
}
params = {
    'user_id': 'REPA0586',
}

response = requests.get(url, headers=headers, params=params)

if response.status_code == 200:
    data = response.json()
    print(data)
else:
    print('Failed to retrieve statistics:', response.status_code, response.text)