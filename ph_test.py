from http_util import *
from data.ph import *


print(query(RootQueryType.get(), port=4000, sufix='/beta/betausers'))
print(query(RootMutationType().newBetaUser(email="hi@l.there",
                                           note='whaterve'), port=4000, sufix='/beta/betausers'))
