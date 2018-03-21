import requests
import pprint
from data.test import *

from collections import defaultdict

pool = defaultdict(set)


def collect_values(hash_map):
    for k, v in hash_map.items():
        if isinstance(v, dict):
            collect_values(v)
            continue
        elif isinstance(v, list):
            for val in v:
                if isinstance(val, dict):
                    return collect_values(val)
                pool[k].add(val)
            continue
        pool[k].add(v)
    return


def query(opt):
    print(">> ", opt)
    url = 'http://localhost:9002/graphql'
    json = {
        'query': opt
    }
    headers = {'Authorization': 'None'}

    r = requests.post(url=url, json=json, headers=headers)
    # pprint.pprint(r.json())
    assert r.ok, r
    collect_values(r.json())
    return r


# query(Employee().get())
# query(Query().company(1))
# query(Query().company(2))
# query(Query().employee(3))

def test_query():
    query(Query.get())


def test_segment():
    query(Segment().get())


def test_offers():
    query(Query().allOffers(filter='null'))


def test_offers_none():
    query(Query().allOffers(filter=None))


def test_company():
    query(Query().company(id='"5"'))


print(Segment().__class__.__name__)
