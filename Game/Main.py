'''
Created on Apr 30, 2018

@author: jfernando
'''
from Deck import Deck
from Card import Card, Suit, Value
from Set import Set
from Hand import Hand
from Player import Player
from Blackjack import Blackjack

playerCount = int(input("How many Players? "))
players = []
for p in range(1,playerCount+1):
    players.append(Player(input("Player " + str(p) + ", what's your name? ")))
extraDeckCount = int(input("How many decks? ")) - 1
while input("Ready to Play? ") != "NO":
    Blackjack().play(extraDeckCount,players)
    for p in players:
        p.hands = []
        print("Player " + p.name + " you have $" + str(p.cash))