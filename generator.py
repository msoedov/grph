from jinja2 import Template

# >> > s = "{% for element in elements %}{{loop.index}} {% endfor %}"
# >> > Template(s).render(elements=["a", "b", "c", "d"])

headers = Template("""
{% for t in spec %}{{t.name}}{% if not loop.last %} = {% endif %}{% endfor %} = None

""")

# Todo: topological sort

types_decl = Template("""
class {{name}}(object):
    \"""[summary]
    \"""
{% for f in fields %}
    {{ f['name'] }}:{{ f['etype'] }} = {{f.defaultValue or None}}
{% endfor %}
{% for f in input_fields %}
    \"""{{f.description}}\"""
    {{ f['name'] }}:{{ f['etype'] }} = {{f.defaultValue}}
{% endfor %}
{% for f in enums %}
    \"""{{f.description}}\"""
    {{ f.name }} = "{{f.name}}"
{% endfor %}

{% for m in methods %}
    def {{ m['name'] }}({% for a in m['args'] %}{{a.name}}:{{a.etype}}{% if not loop.last %}, {% endif %}{% endfor %}):
        \"""
        {{m['description']}}
        \"""
{% endfor %}
""")


def know_types(t):
    mapping = {
        'String': 'str',
        'Boolean': 'bool',
        'Intger': 'int',
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
    if ts.get('kind') == 'ENUM':
        return ts['name']
    if ts.get('args'):
        return"Method"
    if ts.get('kind') == "SCALAR":
        return ts['name']
    subKind = ts.get('type') or ts.get('ofType')
    if not subKind:
        return "map"
        # raise ValueError(ts)
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
    return ts


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
        print(types_decl.render(
            name=thing['name'],
            fields=Fields(thing),
            methods=Methods(thing),
            input_fields=InputFields(thing),
            enums=EnumValues(thing),
        ))
