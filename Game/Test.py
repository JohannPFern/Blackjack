'''
Created on Apr 23, 2018

@author: jfernando
'''
from Deck import Deck
from Card import Card, Suit, Value
from Set import Set
from Hand import Hand

test = Deck()
print(str(test.len()) + Set.print(test))
test.add52()
print(str(test.len()) + Set.print(test))
bop = Hand("Pablo")
for x in range(0,20):
    test.shuffle()
    bop.add(test.giveRand())
print(str(len(test.contents) + len(bop.contents)) + test.print() + "|" + bop.print())
print(str(len(test.contents)) + "|" + str(len(bop.contents)))
bop.giveAll(test)
print(str(len(test.contents)) + "|" + str(len(bop.contents)))
