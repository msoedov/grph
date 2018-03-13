from collections import namedtuple
from jinja2 import Template

# >> > s = "{% for element in elements %}{{loop.index}} {% endfor %}"
# >> > Template(s).render(elements=["a", "b", "c", "d"])

headers = Template("""
{% for t in spec %}{{t.name}}{% if not loop.last %} = {% endif %}{% endfor %} = None

""")

types_decl = Template("""
class {{node.name}}({{node.derives()}}):
    \"""
    {{node.description}}
    \"""
{% for f in node.fields %}
    {{ f.name }}:{{ f.etype }} = {{f.defaultValue or None}}
{% endfor %}
{% for f in node.input_fields %}
    \"""{{f.description}}\"""
    {{ f.name }}:{{ f.etype }} = {{f.defaultValue}}
{% endfor %}
{% if node.is_enum() %}
    __enum__ = True
{% endif %}
{% for f in node.enums %}
    \"""{{f.description}}\"""
    {{ f.name }} = "{{f.name}}"
{% endfor %}
{% for m in node.methods %}
    def {{ m.name }}({% for a in m.args %}{{a.name}}:{{a.etype}}{% if not loop.last %}, {% endif %}{% endfor %}) -> {{m.etype}}:
        \"""
        {{m.description}}
        \"""
{% endfor %}
""")


def know_types(t):
    mapping = {
        'String': 'str',
        'Boolean': 'bool',
        'Int': 'int',
    }
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
    if ts.get('kind') == 'OBJECT':
        return ts['name']
    if ts.get('kind') == 'INTERFACE':
        return ts['name']
    if ts.get('kind') == 'INPUT_OBJECT':
        return ts['name']
    if ts.get('kind') == 'UNION':
        return ts['name']
    if ts.get('kind') == 'ENUM':
        return ts['name']
    if ts.get('args'):
        return"Method"
    if ts.get('kind') == "SCALAR":
        return ts['name']
    subKind = ts.get('type') or ts.get('ofType')
    if not subKind:
        raise ValueError(ts)
    if subKind['kind'] == 'LIST':
        subT = of_type(ts.get('type') or ts.get('ofType'))
        return'[{}]'.format(subT)
    if subKind['name']:
        return subKind['name']
    return subKind['ofType']['name']


def methodF(ts):
    """
    """
    args = ts['args']
    ts['args'] = [dict(name=a['name'], etype=guess_type(a['type']))
                  for a in args]
    ts['etype'] = guess_type(ts.get("type"))
    return ts


class Node(namedtuple('Node', ['name', 'description', 'fields', 'methods', 'enums', 'input_fields'])):
    """[summary]

    Arguments:
        namedtuple {[type]} -- [description]
    """

    def derives(self):
        mapping = {
            'String': 'str',
            # 'Boolean': 'bool',
            'Int': 'int',
            'ID': 'str'
        }
        # Fix date time
        if self.name in mapping:
            return mapping[self.name]
        if not self.fields and not self.methods and not self.enums and not self.input_fields:
            return 'str'
        return 'object'

    def is_enum(self):
        return bool(self.enums)


def Fields(t):
    fields = t['fields']
    if not fields:
        return []
    for f in fields:
        f['etype'] = guess_type(f)
    return [f for f in fields if f.get('args', []) == []]


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

    fields = t.get('inputFields')
    if not fields:
        return []
    for f in fields:
        f['etype'] = guess_type(f)
    return fields


def EnumValues(t):
    fields = t.get('enumValues') or []
    return fields


def Methods(t):
    fields = t['fields'] or []
    methods = [methodF(f) for f in fields if f.get('args')]
    return methods


def show(spec):

    print(headers.render(spec=spec['types']))
    for thing in spec['types']:
        if thing['name'].startswith('__'):
            continue
        node = Node(
            name=thing['name'],
            description=thing['description'],
            fields=Fields(thing),
            methods=Methods(thing),
            input_fields=InputFields(thing),
            enums=EnumValues(thing),
        )
        print(types_decl.render(node=node))
