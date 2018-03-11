from jinja2 import Template

# >> > s = "{% for element in elements %}{{loop.index}} {% endfor %}"
# >> > Template(s).render(elements=["a", "b", "c", "d"])

headers = """
def Var(name): return name
"""


types_decl = Template("""
class {{name}}(object):
{% for f in fields %}
    {{ f['name'] }} = Var({{ f['etype'] }})
{% endfor %}

{% for m in methods %}
    def {{ m['name'] }}({% for a in m['args'] %}{{a.name}}:{{a.etype}}{% if not loop.last %}, {% endif %}{% endfor %}):
        \"""
        {{m['description']}}
        \"""
{% endfor %}
""")


def guess_type(ts):
    """
    >>> {'kind': 'OBJECT', 'name': 'User', 'ofType': None}
    User
    >>> {'kind': 'NON_NULL', 'name': None, 'ofType': {'kind': 'SCALAR', 'name': 'String', 'ofType': None}}
    String
    """
    if ts.get('kind') == 'OBJECT':
        return ts['name']
    if ts.get('args'):
        return"Method"
    if ts.get('kind') == "SCALAR":
        return ts['name']
    subKind = ts.get('type') or ts.get('ofType')
    if not subKind:
        return "None?"
        # raise ValueError(ts)
    if subKind['kind'] == 'LIST':
        subT = guess_type(ts.get('type') or ts.get('ofType'))
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


def Methods(t):
    fields = t['fields'] or []
    methods = [methodF(f) for f in fields if f.get('args')]
    return methods


def show(spec):
    for thing in spec['types']:
        if thing['name'].startswith('__'):
            continue
        print(types_decl.render(
            name=thing['name'],
            fields=Fields(thing),
            methods=Methods(thing)),
        )
