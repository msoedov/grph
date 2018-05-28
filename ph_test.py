from http_util import *
from data.ph import *


def endpoint(q):
    return guery(q, port=4000, sufix='/beta/betausers')


print(BetaUser())

print(query.get())
print(endpoint(query.get()))
print(endpoint(mutation.newBetaUser(
    email="hi@l.there", note='non empty')))
