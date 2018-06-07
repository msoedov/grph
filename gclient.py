import pprint
from collections import defaultdict

import requests

import data.ph as ph
from data.test import *

pool = defaultdict(set)


def serialize(obj):
    if not hasattr(obj, "render"):
        return json.dumps(obj)

    vals = obj.render()
    buf = "{" + ", ".join([f"{n}:{serialize(v)}" for n,
                           v in vals.items()]) + "}"
    return buf


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
    url = "http://localhost:9002/graphql"
    json = {"query": opt}
    headers = {"Authorization": "None"}

    r = requests.post(url=url, json=json, headers=headers)
    pprint.pprint(r.json())
    assert r.ok, r
    collect_values(r.json())
    return r


def test_query():
    query(Query.get())


# def test_segment():
#     query(Employee().get())


# def test_offers():
#     query(Company().get())


# def test_offers_with_filter():
#     query(Query().company(id=None))
