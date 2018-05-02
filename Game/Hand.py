'''
Created on Apr 25, 2018

@author: jfernando
'''
from Card import Card, Suit, Value
import abc
from Set import Set

class Hand(Set):
    
    def __init__(self):
        self.contents = []
        
    def eval(self):
        value = 0
        aces = 0
        for c in self.contents:
            value += c.val()
            if c.val() == 11:
                aces += 1
        while value > 21 and aces > 0:
            value -= 10
            aces -= 1
        return value
    