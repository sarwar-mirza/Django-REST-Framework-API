import requests
import json

URL = "http://127.0.0.1:8000/studentapi/"

# get request
def get_data(id = None):
    data = {}
    
    if id is not None:
        data = {'id': id}
        
    json_data = json.dumps(data)  # json data convert from complex data
    r = requests.get(url= URL, data = json_data)
    data = r.json()
    
    print(data)

get_data(2)


# post request
def post_data():
    data = {
        'name': 'Pinky',
        'roll': 105,
        'city': 'Shariyatpur',
    }
    
    json_data = json.dumps(data)
    r = requests.post(url= URL, data= json_data)
    data = r.json()
    
    print(data)

# post_data()


# update request
def update_data():
    data = {
        'id': 4,
        'name': 'Bristy',
        'city': 'Shariyatput',
    }
    
    json_data = json.dumps(data)
    r = requests.put(url= URL, data= json_data)
    data = r.json()
    
    print(data)

# update_data()


# delete request
def delete_data():
    data = {
        'id': 5,
    }
    
    json_data = json.dumps(data)
    r = requests.delete(url= URL, data= json_data)
    data = r.json()
    
    print(data)
delete_data()

