import data.ph as ph
import data.test as t
from grph.http import guery


def endpoint(q):
    return guery(q, port=4000, sufix='/beta/betausers')


def test_ph():
    print(ph.BetaUser())

    print(ph.query.get())
    print(endpoint(ph.query.get()))
    print(endpoint(ph.mutation.newBetaUser(
        email="hi@l.there", note='non empty')))


# def test_query():
#     endpoint(t.Query.get())


# def test_segment():
    # endpoint(t.Employee().get())


# def test_offers():
    # endpoint(t.Company().get())
