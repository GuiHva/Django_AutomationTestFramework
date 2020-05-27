import requests

'''
Use requests to simulate HTTP requests to get API data

API:
    /api/consumable/lists
Host:
    http://127.0.0.1:8000
'''

Host = 'http://127.0.0.1:8000'
API_path = '/api/get_event_list/'
r = requests.get(Host + API_path, auth = ('test','test123456'), params={'eid':'1'})
result = r.json()
print(result)