import sys
from collections import namedtuple
import render
from attrdict import AttrDict as D


BasicTypes = set(["String", "Int", "Boolean", "Float", "ID"])
AST = {}
ETYPE = "etype"
RANK0 = "rank0"


def know_types(t):
    mapping = {"String": "str", "Boolean": "bool", "Int": "int"}
    return mapping.get(t, t)


def guess_type(ts):
    return know_types(of_type(ts))


def of_type(ts):
    """
    >>> of_type({'kind': 'OBJECT', 'name': 'User', 'ofType': None})
    'User'
    >>> of_type({'kind': 'NON_NULL', 'name': None, 'ofType': {'kind': 'SCALAR', 'name': 'String', 'ofType': None}})
    'String'
    >>> of_type({"kind": "ENUM", "name": "ProjectState"})
    'ProjectState'
    """
    if ts.get("kind") == "OBJECT":
        return ts["name"]

    if ts.get("kind") == "INTERFACE":
        return ts["name"]

    if ts.get("kind") == "INPUT_OBJECT":
        return ts["name"]

    if ts.get("kind") == "UNION":
        return ts["name"]

    if ts.get("kind") == "ENUM":
        return ts["name"]

    if ts.get("args"):
        return "Method"

    if ts.get("kind") == "SCALAR":
        return ts["name"]

    subKind = ts.get("type") or ts.get("ofType")
    if not subKind:
        raise ValueError(ts)

    if subKind["kind"] == "LIST":
        subT = of_type(ts.get("type") or ts.get("ofType"))
        return "[{}]".format(subT)

    if subKind["name"]:
        return subKind["name"]

    return subKind["ofType"]["name"]


def methodF(ts):
    """
    """
    args = ts["args"]
    ts["args"] = [dict(name=a["name"], etype=guess_type(a["type"]))
                  for a in args]
    ts[ETYPE] = guess_type(ts.get("type"))
    return ts


def sorted_fields(fs):
    return sorted(map(D, fs), key=lambda x: x["name"])


class Node(
    namedtuple(
        "Node", ["name", "description", "fields",
                 "methods", "enums", "input_fields"]
    )
):
    """[summary]

    Arguments:
        namedtuple {[type]} -- [description]
    """

    def derives(self):
        mapping = {
            "String": "str",
            # 'Boolean': 'bool',
            "Int": "int",
            "ID": "str",
        }
        # Fix date time
        if self.name in mapping:
            return mapping[self.name]

        if not self.fields and not self.methods and not self.enums and not self.input_fields:
            return "str"

        return "node"

    def is_enum(self):
        return bool(self.enums)

    def is_composite_t(self):
        return self.derives() == "node"

    def all_fields(self):
        return sorted_fields(self.fields + self.input_fields)

    def all_annot_fields(self):
        fs = [f for f in self.all_fields() if f['name'] not in set(
            ['str', 'bool', 'int', 'float'])]
        return fs

    def flatern(self, rank=-1):
        fields = self.all_fields()

        def simple(name):
            return name.strip("[]") if name else name

        if rank == 0:
            return "{" + " ".join(
                [f["name"] for f in fields if simple(f[ETYPE]) not in AST]
            ) + "}"

        return "{" + " ".join(
            [f["name"] if f[ETYPE] not in AST else "{}" for f in fields]
        ) + "}"


def Fields(t):
    fields = t["fields"]
    if not fields:
        return []

    for f in fields:
        f[ETYPE] = guess_type(f)
    return sorted_fields([f for f in fields if f.get("args", []) == []])


def InputFields(t):
    """
    "name": "clientMutationId",
    "description": "A unique identifier for the client performing the mutation.",
    "type": {
        "kind": "SCALAR",
        "name": "String",
        "ofType": null
    },
    "defaultValue": null
    """

    fields = t.get("inputFields")
    if not fields:
        return []

    for f in fields:
        f[ETYPE] = guess_type(f)
    return sorted_fields(fields)


def EnumValues(t):
    fields = t.get("enumValues") or []
    return fields


def Methods(t):
    fields = t["fields"] or []
    methods = [methodF(f) for f in fields if f.get("args")]
    return methods


def queryType(s):
    return (s.get('queryType', {}) or {}).get('name', '')


def mutationType(s):
    return (s.get('mutationType', {}) or {}).get('name', '')


def show(spec):
    def special(x): return x["name"].startswith("__")

    variables = [t for t in spec["types"] if not special(t)]

    # print(headers.render(spec=variables))
    print(render.headers(spec=variables))
    nodes = []
    qt = queryType(spec)
    mt = mutationType(spec)
    for thing in spec["types"]:
        if special(thing) or thing["name"] in BasicTypes:
            continue

        node = Node(
            name=thing["name"],
            description=thing["description"],
            fields=Fields(thing),
            methods=Methods(thing),
            input_fields=InputFields(thing),
            enums=EnumValues(thing),
        )
        nodes.append(node)
        AST[node.name] = node
    for node in nodes:
        print(render.render(node=node))
        # print(types_decl.render(node=node) or '')
