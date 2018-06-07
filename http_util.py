import pprint
from collections import defaultdict

import requests

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


def guery(opt, port=9002, sufix='graphql'):
    print("Query >> ", opt)
    url = f"http://localhost:{port}/{sufix}"
    json = {"query": opt}
    headers = {"Authorization": "None"}

    r = requests.post(url=url, json=json, headers=headers)
    if not r.ok:
        pprint.pprint(r.content[:200])
    pprint.pprint(r.json())
    assert r.ok, r
    collect_values(r.json())
    return r
