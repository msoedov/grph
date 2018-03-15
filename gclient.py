import requests

from data.test import *


def query(opt):
    print(opt)
    url = 'http://localhost:9002/graphql'
    json = {
        'query': opt
    }
    headers = {'Authorization': 'None'}

    r = requests.post(url=url, json=json, headers=headers)
    print(r.text)


query(Employee().get())
query(Query().company(1))
query(Query().company(2))
query(Query().employee(3))
