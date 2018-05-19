import json
import sys

__all__ = ('define', 'node')


def define(name, names):
    ns = sys.modules[name]
    for name in names:
        if name == 'ID':
            continue
        setattr(ns, name, name)


def dumps(name, obj, level=1):
    ns = sys.modules[name]
    annot = obj.__annotations__
    t = obj.__class__

    def value_helper(v):
        if isinstance(v, list):
            v = v[0]
        if isinstance(v, str):
            v = getattr(ns, v, v)
        if isinstance(v, list):
            v = v[0]
        return v
    annot = {k: value_helper(v) for k, v in annot.items()}
    if level <= 0:
        annot = {k: v for k, v in annot.items(
        ) if v and not hasattr(v, '__annotations__')}
    ret = '{' + ' '.join(n + " " + dumps(name, klass, level=level-1) if hasattr(
        klass, '__annotations__') else n
        for n, klass in annot.items()) + '}'
    return ret


def serialize(obj):
    if not hasattr(obj, 'render'):
        return json.dumps(obj)
    vals = obj.render()
    buf = '{' + ', '.join([f'{n}:{serialize(v)}' for n,
                           v in vals.items()]) + '}'
    return buf


class node(object):
    def __init__(self, **kwargs):
        [setattr(self, name, kwargs.pop(name, val))
         for name, val in self.render().items()]

    @classmethod
    def F(self):
        return dumps(self.__class__.__module__, self)

    @classmethod
    def get(self):
        return self.wrap(dumps(self.__class__.__module__, self))

    @classmethod
    def wrap(self, subquery, fn=False, **kwargs):
        if kwargs:
            _kwargs = {name: serialize(val) for name, val in kwargs.items()}
            _kwargs['ret'] = kwargs.get('ret', None)
            subquery = subquery % _kwargs
        subquery = subquery.replace('"null"', 'null')
        if fn:
            return check_modifier(self) + " {" + subquery + " } "
        if is_root(self):
            return subquery
        return "{ " + self.__name__.lower() + subquery + "}"

    def __str__(self):
        return json.dumps(self.render())


def is_root(klass):
    return 'query' in klass.__name__.lower() or 'mutation' in klass.__name__.lower()


def check_modifier(klass):
    if 'mutation' in klass.__name__.lower():
        return 'mutation'
    return klass.__name__


class ID(str):

    """
    The `ID` scalar type represents a unique identifier, often used to
refetch an object or as key for a cache. The ID type appears in a JSON
response as a String; however, it is not intended to be human-readable.
When expected as an input type, any string (such as `"4"`) or integer
(such as `4`) input value will be accepted as an ID.
    """

    def render(self):
        return self

    @classmethod
    def F(self):
        return "ID"


def RootOf(module):
    module = sys.modules[module]
    for k, v in vars(module).items():
        if 'query' in k.lower():
            print(k, v)
            return v
    raise NameError('No query def found!')
