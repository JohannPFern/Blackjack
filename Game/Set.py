'''
Created on Apr 23, 2018

@author: jfernando
'''
import random
from abc import ABC

class Set(ABC):
        
    def shuffle(self):
        random.shuffle(self.contents)
    
    def add(self, c):
        self.contents.append(c)
        
    def len(self):
        return len(self.contents)
        
    def giveRand(self):
        if len(self.contents) > 0:
            return self.contents.pop(0)
        else:
            return -1
        
    def giveAll(self, base):
        for x in range(0,len(self.contents)):
            base.add(self.contents[x])
        self.contents=[]
               
    def print(self):
        if len(self.contents) == 0:
            return ""
        w = self.contents[0].print()
        for c in range(1,len(self.contents)):
            w += ", " + self.contents[c].print()
        return w
                