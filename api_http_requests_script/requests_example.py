import requests
import json

'''
Use requests to simulate HTTP requests to get API data, use token

API:
    /api/registration/report/lists
Host:
    http://192.168.1.91:20000
'''

Host = 'http://192.168.1.91:20000'
API_path = '/api/registration/report/lists'
headers = {
    'Authorization': 'bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJodHRwOlwvXC8xOTIuMTY4LjEuOTE6MjAwMDBcL2FwaVwvYXV0aFwvbG9naW4iLCJpYXQiOjE1OTA5Nzk0MDMsImV4cCI6MTU5MTU4NDIwMywibmJmIjoxNTkwOTc5NDAzLCJqdGkiOiJzUUphRmdvNFlmNVBwNEJqIiwic3ViIjo1MiwicHJ2IjoiODdlMGFmMWVmOWZkMTU4MTJmZGVjOTcxNTNhMTRlMGIwNDc1NDZhYSJ9.d31FmkfP0h4bf3uaYs5TcVKeZkTD4u6TpnLqza2pz8I'}
r = requests.get(Host + API_path, headers=headers, params={'page_size': '10', 'print_status': '1'})
result = r.json()
with open('result.json', 'w', encoding='utf-8') as f:
    json.dump(result, f)
    print('Done!')
