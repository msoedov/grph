import sys
import json
from .lib import show


def resolve(json_raw):
    data = json.loads(json_raw)['data']['__schema']
    show(data)


if __name__ == '__main__':
    with open(sys.argv[1] if len(sys.argv) > 1 else 'sample.json', 'r') as fp:
        data = fp.read()
        resolve(data)
