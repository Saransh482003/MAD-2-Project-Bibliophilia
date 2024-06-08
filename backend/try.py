import requests

url = 'http://127.0.0.1:5000/get-feedbacks'
headers = {
    'x-access-token': 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJSRVBBMDM1NCIsImlhdCI6MTcxNzc2NzI4NywiZXhwIjoxNzE3Nzg4ODg3fQ.FpoARHw0fYKmwGcSLJBZRYZPvP4VFHRh3H-XbnIE7DY'
}
params = {
    'user_id': 'REPA0354',
}

response = requests.get(url, headers=headers, params=params)

if response.status_code == 200:
    data = response.json()
    print(data)
else:
    print('Failed to retrieve statistics:', response.status_code, response.text)