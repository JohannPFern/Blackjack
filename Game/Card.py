'''
Created on Apr 23, 2018

@author: jfernando
'''
from enum import Enum

class Card(object):
    
    def __init__(self, s, v):
        self.suit = s
        self.value = v
 
    def print(self):
        return(str(self.value.name) + " of " + str(self.suit.name))
    
    def val(self):
        x = self.value.value
        if x == 1:
            x = 11
        elif x > 10:
            x = 10
        return x
   
   
class Suit(Enum):
    SPADES = "S"
    HEARTS = "H"
    CLUBS = "C"
    DIAMONDS = "D"
    
class Value(Enum):
    ACE = 1
    TWO = 2
    THREE = 3
    FOUR = 4
    FIVE = 5
    SIX = 6
    SEVEN = 7 
    EIGHT = 8 
    NINE = 9 
    TEN = 10
    JACK = 11
    QUEEN = 12
    KING = 13     