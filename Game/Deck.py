'''
Created on Apr 23, 2018

@author: jfernando
'''
from Card import Card, Suit, Value 
import abc
from Set import Set

class Deck(Set):

    def __init__(self):
        self.contents = []
        for s in Suit:
            for v in Value:
                self.contents.append(Card(s,v))
    
    def add52(self):
        for s in Suit:
            for v in Value:
                self.contents.append(Card(s,v))      