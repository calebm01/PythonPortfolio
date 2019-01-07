import random


#Initialize lists
deck = []

player1hand = []
player2hand = []

#function that creates the initial deck using for loops
def makedeck(deck):
    """populate the deck of cards"""
    SUITS = ["hearts", "diamonds", "clubs", "spades"]
    VALUES = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
    for e in SUITS:
        for i in VALUES:
            card = i+" "+e
            deck.append(card)

def shuffledeck(deck):
    for i in range(len(deck)):
        j = random.randrange(len(deck))
        temp = deck[i]
        deck[i] = deck[j]
        deck[j] = temp
        
def dealing(deck,player1hand,player2hand):
    for i in range(5):
        card = deck.pop(0)
        player1hand.append(card)
        card = deck.pop(0)
        player2hand.append(card)


makedeck(deck)
print(deck)
shuffledeck(deck)
print(deck)
print(len(deck))
dealing(deck,player1hand,player2hand)

print("\n Here's your hand: ", player1hand)
print("\n Here's your hand:", player2hand)
