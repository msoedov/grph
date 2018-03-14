from spec import *


def Graph(*subqueries) -> str:
    return "viewer {\n" + "\n".join(subqueries) + "\n}"


def test_to_query():
    print(Query().license("foo"))


def test_render():
    assert User().render() != {}


def test_ID_query():
    assert ID("id").render() == "id"


def test_ID_F():
    assert ID().F() == "ID"


def test_combined():
    assert Graph(Query().license("foo"), Query().codeOfConduct("myRepo")) != ""
