import requests

from data.test import *

url = 'http://localhost:9002/graphql'
json = {
    'query': Employee().get_short()
}
headers = {'Authorization': 'None'}

r = requests.post(url=url, json=json, headers=headers)
print(r.text)
