import requests
import json

URL = "http://127.0.0.1:8000/stucreate/"     # url write now

data = {
    'name': 'Sadiya Haque',
    'roll': 101,
    'city': 'Dhaka',
}

json_data = json.dumps(data)    # json data convert from python data using dumps() method

r = requests.post(url = URL, data= json_data)    # Post request

data= r.json()

print(data)