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


def Val(name):
    if name in pool:
        return pool[name].pop()
    return "?"


def query(opt):
    print(">> ", opt)
    url = 'http://localhost:9002/graphql'
    json = {
        'query': opt
    }
    headers = {'Authorization': 'None'}

    r = requests.post(url=url, json=json, headers=headers)
    pprint.pprint(r.json())
    assert r.ok, r
    collect_values(r.json())
    return r


def test_query():
    query(Query.get())


def test_segment():
    query(Segment().get())


def test_offers():
    query(Query().allOffers(filter='null'))


def test_offers_none():
    query(Query().allOffers(filter=None))


def test_company():
    query(Query().company(id='5'))


def test_mutation():
    query(Mutation().createUser(name="Ivan", password="Govnov", email="null",
                                role=None, picture=":",
                                active=True,
                                readonly=True,
                                emailNotification=False, companyId=""))


def test_mutation_v2():
    query(Mutation().createUser(name=Val('name'),
                                password=Val('password'),
                                email=Val('email'),
                                role=None,
                                picture=":",
                                active=True,
                                readonly=True,
                                emailNotification=False,
                                companyId=""))
