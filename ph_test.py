from http_util import *
from data.ph import *


def endpoint(q):
    return query(q, port=4000, sufix='/beta/betausers')


print(BetaUser())

print(endpoint(RootQueryType.get()))
print(endpoint(RootMutationType().newBetaUser(
    email="hi@l.there", note='non empty')))
