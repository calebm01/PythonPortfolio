#Blackjack
#Demonstrates combining objects
#Caleb Mouritsen
#2/5/19

import random

class card(object):
    #A playing card
    #This class will build a single card
    RANKS = ["A", "2", "3", "4", "5", "6", "7",
             "8", "9", "10", "J", "Q", "K"]
    SUITS = ["♣", "♦", "♥", "♠"]

    def __init__(self,rank,suit, face_up):
        self.rank = rank
        self.suit = suit
        self.is_face_up = face_up

    def __str__(self):
        if self.is_face_up:
            rep = self.rank + self.suit
        else:
            rep = "XX"
        return rep
    
    def flip(self):
        self.is_face_up = not self.is_face_up

class Hand(object):
    #A hand of playing cards
    def __init__(self):
        self.cards = []

    def __str__(self):
        if self.cards:
            rep = ""
            for card in self.cards:
                rep += str(card) + " "
        else:
            rep = "<empty>"
        return rep

    def clear(self):
        self.cards = []

    def add(self, card):
        self.cards.append(card)

    def give(self, card, other_hand):
        self.cards.remove(card)
        other_hand.add(card)

class Deck(Hand):
    #A deck of playing cards
    #This class has three methods. populate, shuffle, and deal
    #populate is the beginning method. self is passed in
    #for loops are used to sort through the suits and ranks, and then the card is determined to be positionable or not
    #add card to hand
    #shuffle method which imports random and then randomizes the cards list
    def populate(self):
        for suit in Card.SUITS:
            for rank in Card.RANKS:
                card = Card(rank,suit,False)
                self.add(card)

    def shuffle(self):
        import random
        random.shuffle(self.cards)
            
    def deal(self,hands,per_hand=5):
        for rounds in range(per_hand):
            for hand in hands:
                if self.cards:
                    top_card = self.cards[0]
                    self.give(top_card, hand)

                else:
                    print("Can't continue to deal. Out of cards!")


if __name__== "__main__":
    print("You ran this module directly (and did not import it)")
    input("\n\nPress the enter key to exit.")
          
