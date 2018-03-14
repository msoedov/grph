# trafaret reflection
import json
import re
import sys

import trafaret as t

import collections
import generator

iso8601 = re.compile(
    r'^(?P<full>((?P<year>\d{4})([/-]?(?P<mon>(0[1-9])|(1[012]))([/-]?(?P<mday>(0[1-9])|([12]\d)|(3[01])))?)?(?:T(?P<hour>([01][0-9])|(?:2[0123]))(\:?(?P<min>[0-5][0-9])(\:?(?P<sec>[0-5][0-9]([\,\.]\d{1,10})?))?)?(?:Z|([\-+](?:([01][0-9])|(?:2[0123]))(\:?(?:[0-5][0-9]))?))?)?))Z$')


def indentation(indent):
    return " " * 4 * indent
    # return ""


def List(t, indent=0):
    # t = ' | '.join(set(t))
    return indentation(indent=indent) + 't.List({})'.format(t)


def Float(*a, indent=0):
    return indentation(indent=indent) + 't.Float()'


def Int(*a, indent=0):
    return indentation(indent=indent) + 't.Int()'


def Any(*a, indent=0):
    return indentation(indent=indent) + 't.Any()'


def String(*a, indent=0):
    return indentation(indent=indent) + 't.String()'


def Regexp(exp, indent=0):
    return indentation(indent=indent) + 't.String(regex={})'.format(exp)


def Email(*a, indent=0):
    return indentation(indent=indent) + 't.Email()'


def Dict(keys, indent=0):
    return indentation(indent=indent) + 'D({' + ',\n    '.join(keys) + '}\n)'


def Key(name, indent=0):
    return indentation(indent=indent) + "t.Key('{}'): ".format(name)


def Null(*a, indent=0):
    return indentation(indent=indent) + 't.Null()'


def match(thing, indent=0):
    if isinstance(thing, list):
        if not len(thing):
            return List(Any(indent+1), indent=indent)
        return List(match(thing[0]), indent=indent)
    elif isinstance(thing, int):
        return Int(indent=indent)
    elif isinstance(thing, float):
        return Float(indent=indent)
    elif isinstance(thing, str):
        ip_pattern = '^(?:[0-9]{1,3}\.){3}[0-9]{1,3}$'

        if '@' in thing:
            return Email(indent=indent)
        elif re.match(pattern=ip_pattern, string=thing):
            return Regexp(exp=ip_pattern)
        elif re.match(pattern=iso8601, string=thing):
            return Regexp(exp=iso8601)
        return String(indent=indent)
    elif isinstance(thing, dict):
        return Dict([Key(name) + match(value, indent=indent + 1) for name, value in thing.items()])
    elif thing is None:
        return Null()
    raise ValueError(thing)


def resolve(json_raw):
    pre = """import trafaret as t\ndef D(x): return t.Dict(x).allow_extra('*')\nschema="""
    data = json.loads(json_raw)['data']['__schema']
    print(generator.show(data))
    return pre + match(data)


def main():
    body = ""

    while True:
        k = input()
        if not k:
            break
        body = body + k
    print('')

    resolve(body)


if __name__ == '__main__':
    with open(sys.argv[1] if len(sys.argv) > 1 else 'sample.json', 'r') as fp:
        data = fp.read()
        (resolve(data))
