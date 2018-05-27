import json
import sys

__all__ = ('define', 'node', 'ID', 'sig')


def sig(t):
    if isinstance(t, list):
        t = t[0]
    if hasattr(t, 'F'):
        return t.F()
    return None


def define(name, names):
    ns = sys.modules[name]
    for name in names:
        if name == 'ID':
            continue
        setattr(ns, name, name)


def dumps(name, obj, level=2):
    ns = sys.modules[name]
    annot = obj.__annotations__

    def value_helper(v):
        if isinstance(v, list):
            v = v[0]
        if isinstance(v, str):
            v = getattr(ns, v, v)
        if isinstance(v, list):
            v = v[0]
        return v

    def is_annotated(_klass):
        _klass = _klass[0] if isinstance(_klass, list) else _klass
        if isinstance(_klass, str):
            _klass = getattr(ns, _klass, _klass)
        return hasattr(_klass, '__annotations__')

    annot = {k: value_helper(v) for k, v in annot.items()}
    print('an', repr(annot), ns)
    if level <= 0:
        annot = {k: v for k, v in annot.items(
        ) if v and not hasattr(v, '__annotations__')}
    ret = '{' + ' '.join(n + " " + dumps(name, klass, level=level-1) if is_annotated(klass) else n
                         for n, klass in annot.items()) + '}'
    return ret


def serialize(obj):
    if not hasattr(obj, 'render'):
        return json.dumps(obj)
    vals = obj.render()
    if not any(*vals.values()):
        vals = obj.signature()
        raise NameError("Watch this")

    buf = '{' + ', '.join([f'{n}:{serialize(v)}' for n,
                           v in vals.items()]) + '}'
    return buf


class node(object):

    def __init__(self, **kwargs):
        [setattr(self, name, kwargs.pop(name, val))
            for name, val in self.render().items()]
        # raise NameError

    @classmethod
    def F(self):
        module = self.__class__.__module__ if self.__class__.__name__ != 'type' else self.__module__
        return dumps(module, self)

    @classmethod
    def get(self):
        module = self.__class__.__module__ if self.__class__.__name__ != 'type' else self.__module__
        return self.wrap(dumps(module, self))

    @classmethod
    def wrap(self, subquery, fn=False, **kwargs):
        if kwargs:
            _kwargs = {name: serialize(val)
                       for name, val in kwargs.items()}
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
