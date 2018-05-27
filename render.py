from contextlib import contextmanager
from attrdict import AttrDict as D
import sys


class Helpers:

    @classmethod
    def debug(self, t):
        print(repr(t), file=sys.stderr)

    @classmethod
    def clever_type(self, a):
        if not a:
            return None

        return f"'{a}'"

    @classmethod
    def clever_name(self, a):
        if a[0].islower():
            return a.capitalize()

        return a


class DSL:

    def __init__(self):
        self._lines = []
        self._indent = 0

    def add(self, string, *args, **kwargs):
        line = ' ' * self._indent * 4 + string  # .format(*args, **kwargs)
        self._lines.append(line.rstrip(' '))

    def endblock(self):
        return self.add('')

    def endblock_if(self, cond):
        if cond:
            self.add('')

    @contextmanager
    def indent(self):
        self._indent += 1
        try:
            yield
        finally:
            self._indent -= 1

    def content(self):
        return '\n'.join(self._lines)


def headers(spec):
    b = DSL()
    b.add(f'from core_graph import *')
    b.endblock()
    b.add(f'define(__name__, [')
    with b.indent():
        for t in spec:
            t = D(t)
            b.add(f'"{t.name}",')
    b.add('])')
    b.endblock()
    return b.content()


def render(node):
    b = DSL()
    b.add(f'class {node.name}({node.derives()}):')
    with b.indent():
        if node.description:
            b.add('"""')
            b.add(f'{node.description}')
            b.add('"""')
            b.endblock()

        if node.is_enum():
            b.add('__enum__ = True')

        for f in node.fields:
            b.add(
                f'{ f.name }:{ f.etype } = {Helpers.clever_type(f.get("defaultValue"))}')
        # b.endblock_if(node.fields)

        for f in node.input_fields:
            f = D(f)
            if f.description:
                b.add('"""')
                b.add(f'{f.description}')
                b.add('"""')
            b.add(
                f'{ f.name }:{ f.etype } = {Helpers.clever_type(f.get("defaultValue"))}')
        # b.endblock_if(node.input_fields)
        for f in node.enums:
            f = D(f)
            if f.description:
                b.add('"""')
                b.add(f'{f.description}')
                b.add('"""')
            b.add(
                f'{Helpers.clever_name(f.name)} = "{f.name}"')
        # b.endblock_if(node.enums)

        for m in node.methods:
            b.endblock()
            m = D(m)
            arg_to_type = [
                f'{a["name"]}:{a["etype"]}' for a in m.get('args', [])]
            arg_to_fmt = [
                f'{a["name"]}:%({a["name"]})s' for a in m.get('args', [])]
            arg_to_name = [
                f'{a["name"]}={a["name"]}' for a in m.get('args', [])]
            b.add(f'def {m.name}(self, {", ".join(arg_to_type)}) -> {m.etype}:')
            with b.indent():
                if m.description:
                    b.add('"""')
                    b.add(f'{m.description}')
                    b.add('"""')
                b.add(f'tmpl = "{m.name}({", ".join(arg_to_fmt)}) %(ret)s"')
                b.add(
                    f'return self.wrap(tmpl, fn=True, {", ".join(arg_to_name)}, ret={m.etype}.F())')
        if node.is_composite_t():
            b.endblock()
            b.add('def render(self):')

            with b.indent():
                mapping = [
                    f'{f["name"]}=self.{f["name"]}' for f in node.all_fields()]
                b.add(f'return dict({", ".join(mapping)})')
            b.endblock()
        else:
            b.endblock()
            b.add('def render(self):')
            with b.indent():
                b.add('return self')
            b.endblock()
            b.add('@classmethod')
            b.add('def F(self):')
            with b.indent():
                b.add(f'return "{node.name}"')

    b.endblock()
    b.endblock()
    return b.content()
