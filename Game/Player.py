'''
Created on May 2, 2018

@author: jfernando
'''

class Player(object):

    def __init__(self, n):
        self.name = n
        self.hands = []
        self.cash = 100
        
    def addHand(self, h):
        self.hands.append(h)
        