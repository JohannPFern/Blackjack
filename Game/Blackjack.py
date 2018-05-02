'''
Created on May 2, 2018

@author: jfernando
'''
from Deck import Deck
from Card import Card, Suit, Value
from Set import Set
from Hand import Hand
from Player import Player
class Blackjack(object):

    def __init__(self):
        pass
    
    @classmethod   
    def play(self, extraDeckCount, players):
        shoe = Deck()
        for d in range(0,extraDeckCount):
            shoe.add52()
        shoe.shuffle()
        dealer = Hand()
        for p in players:
            v = Hand()
            v.add(shoe.giveRand())
            v.add(shoe.giveRand())
            p.addHand(v)
        dealer.add(shoe.giveRand())
        dealer.add(shoe.giveRand())
        for p in players:
            print("Player " + p.name + ": " + p.hands[0].print())
        print("Dealer: " + dealer.contents[0].print() + ", ? of ?")
        for p in players:
            if p.hands[0].contents[0].value == p.hands[0].contents[1].value:
                i = input("Player " + p.name + " do you wish to split? Hit enter to split, anything else before enter to continue. ")
                if i != "":
                    x = Hand()
                    x.add(p.hands[0].giveRand())
                    p.hands.append(x)
        for p in players:
            for h in p.hands:
                stand = False
                print(h.print())
                while h.eval()<=21 and stand == False:
                    t = input("Player " + p.name + ", do you wish to hit? Type anything to hit, or enter blank to stand. ")
                    if len(t)>0:
                        h.add(shoe.giveRand())
                    else:
                        stand = True
                    print(h.print())
                print(str(h.eval()) + " is Player " + p.name + "'s final value.")
                if (h.eval() == 21 & len(h.contents) == 2):
                    print("Natural Blackjack!")
                if (h.eval()>21):
                    print("Player " + p.name + " busted!")
        print("Dealer " + dealer.print())
        while dealer.eval() < 17:
            dealer.add(shoe.giveRand())
        print("Dealer " + dealer.print())
        d = dealer.eval()
        print("The Dealer's final value is " + str(d) + ".")
        if (len(dealer.contents) == 2):
            print("Natural Blackjack!")
        if (dealer.eval()>21):
            print("The Dealer busted!")
        for p in players:
            for h in p.hands:
                v = h.eval()
                if v == 21 and len(h.contents) == 2 and len(dealer.contents) != 2:
                    print("Player " + p.name + " won $15 with a natural Blackjack!")                   
                    p.cash += 15
                elif v == d:
                    print("Player " + p.name + " tied the dealer.")
                elif v <= 21 and v > d:
                    print("Player " + p.name + " won $10!")
                    p.cash += 10
                elif v <= 21 and d > 21:
                    print("Player " + p.name + " won $10!")
                    p.cash += 10
                else:
                    print("Player " + p.name + " lost $10")
                    p.cash -= 10;
        