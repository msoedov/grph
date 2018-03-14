from spec import *


def test_to_query():
    print(Query().license("foo"))


def test_render():
    assert User().render() != {}


def test_ID_query():
    assert ID("id").render() == "id"


def test_ID_F():
    assert ID().F() == "ID"
