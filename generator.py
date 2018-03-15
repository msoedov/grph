import sys
from collections import namedtuple
from jinja2 import Template


def clever_type(a):
    if not a:
        return None
    return f"'{a}'"


def clever_name(a):
    if a[0].islower():
        return a.capitalize()
    return a


BasicTypes = set(['String', 'Int', 'Boolean'])
AST = {}
ETYPE = 'etype'
RANK0 = 'rank0'

headers = Template("""

{% for t in spec %}
{{t.name}} = "{{t.name}}" {% if not loop.last %} {% endif %}{% endfor %}

def dumps(obj, level=1):
    annot = obj.__annotations__
    t = obj.__class__

    def value_helper(v):
        w = v
        if isinstance(v, list):
            v = v[0]
        if isinstance(v, str):
            v = globals()[v]
        if isinstance(v, list):
            v = v[0]
        return v
    annot = {k: value_helper(v) for k, v in annot.items()}
    if level <= 0:
        annot = {k: v for k, v in annot.items(
        ) if v and not hasattr(v, '__annotations__')}
    ret = '{' + ' '.join(n + " " + dumps(klass, level=level-1) if hasattr(
        klass, '__annotations__') else n
        for n, klass in annot.items()) + '}'
    return ret

""")

types_decl = Template("""
class {{node.name}}({{node.derives()}}):
    \"""
    {{node.description}}
    \"""
{% for f in node.fields %}
    {{ f.name }}:{{ f.etype }} = {{clever_type(f.defaultValue) }} {% endfor %}
{% for f in node.input_fields %}
    \"""{{f.description}}\"""
    {{ f.name }}:{{ f.etype }} = {{ clever_type(f.defaultValue) }} {% endfor %}
{% if node.is_enum() %}
    __enum__ = True
{% endif %}
{% for f in node.enums %}
    \"""{{f.description}}\"""
    {{ clever_name(f.name) }} = "{{f.name}}" {% endfor %}
{% for m in node.methods %}
    def {{ m.name }}(self, {% for a in m.args %}{{a.name}}:{{a.etype}}{% if not loop.last %}, {% endif %}{% endfor %}) -> {{m.etype}}:
        \"""
        {{m.description}}
        \"""
        tmpl = f"{{ m.name }}({% for a in m.args %}{{a.name}}:{ {{a.name}} }{% if not loop.last %}, {% endif %}{% endfor %}) { {{m.etype}}.F() }"
        return self.wrap(tmpl, fn=True)
{% endfor %}

{% if node.is_composite_t() %}
    def render(self):
        return { {% for f in node.all_fields() %}
            "{{ f.name }}": self.{{ f.name }},{% endfor %}
        }

    @classmethod
    def F(self):
        return dumps(self)

    @classmethod
    def get(self):
        return self.wrap(dumps(self))

    @classmethod
    def wrap(self, subquery, fn=False):
        if fn:
            return "{ " + subquery +  " }"
        return "{ {{node.name.lower()}} " + subquery +  " }"
{% else %}
    def render(self):
        return self
    @classmethod
    def F(self):
        return "{{node.name}}"
{% endif %}

""")

types_decl.environment.globals['clever_type'] = clever_type
types_decl.environment.globals['clever_name'] = clever_name


def know_types(t):
    mapping = {
        'String': 'str',
        'Boolean': 'bool',
        'Int': 'int'
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
    ts[ETYPE] = guess_type(ts.get("type"))
    return ts


def sorted_fields(fs):
    return sorted(fs, key=lambda x: x['name'])


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

    def is_composite_t(self):
        return self.derives() == 'object'

    def all_fields(self):
        return sorted_fields(self.fields + self.input_fields)

    def flatern(self, rank=-1):
        fields = self.all_fields()

        def simple(name): return name.strip('[]') if name else name
        if rank == 0:
            return "{" + " ".join([f['name'] for f in fields if simple(f[ETYPE]) not in AST]) + "}"
        return "{" + " ".join([f['name'] if f[ETYPE] not in AST else '{}' for f in fields]) + "}"
        # return "{" + " ".join([f['name'] for f in fields]) + "}"


def Fields(t):
    fields = t['fields']
    if not fields:
        return []
    for f in fields:
        f[ETYPE] = guess_type(f)
    return sorted_fields([f for f in fields if f.get('args', []) == []])


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
        f[ETYPE] = guess_type(f)
    return sorted_fields(fields)


def EnumValues(t):
    fields = t.get('enumValues') or []
    return fields


def Methods(t):
    fields = t['fields'] or []
    methods = [methodF(f) for f in fields if f.get('args')]
    return methods


def show(spec):

    print(headers.render(
        spec=[t for t in spec['types'] if not t['name'].startswith('__')]))
    nodes = []
    for thing in spec['types']:
        if thing['name'].startswith('__') or thing['name'] in BasicTypes:
            continue
        node = Node(
            name=thing['name'],
            description=thing['description'],
            fields=Fields(thing),
            methods=Methods(thing),
            input_fields=InputFields(thing),
            enums=EnumValues(thing),
        )
        nodes.append(node)
        AST[node.name] = node
    # print(AST, file=sys.stderr)
    for node in nodes:
        print(types_decl.render(node=node))
