#  Colton Northcutt,  Parker Dean, Matthew Walker, Caleb Mouritsen
# 2-21-19
# War

import Card, games

class Player(Card.Hand):

    def __init__(self, self):
        self.hand = []
        self.name = name

    def __str__(self):
        rep = self.name
        return rep


class War_card(Card.card):

    @property
    def value(self):
        if self.is_face_up:
            value = Card.RANKS.index(self.rank) + 1
        else:
            value = none
        return value

class War_deck(Card.Deck):
    def populate(self):
        for suit in War_card.SUITS:
            for rank in War_card.RANKS:
                self.cards.append(War_card(rank, suit))

class War_hand(cards.Hand):

    def __init__(self,name):
        super(War_hand,self).__init__()
        self.name
        
class War_game(object):

    def __init__(self,names):
        self.players = []
        for name in names:
            player = War_Player(name)
            self.players.append(player)

        self.pot = War_Pot("pot")
        self.field = War_Field("field")
        self.deck = War_deck.populate
        self.deck = War_deck.shuffle
        
        player_one =  Player(input("Enter player one's name: "))
        player_two = Player(input("Enter player two's name: "))

    def play(self):
        count = 0
        game_over = False
        self.Deck.deal(self.hands,  per_hand = 26)
        input("press enter to play your cards")
        while not game_over:
            try:
                for player in self.players:
                    player.play(self.field)

                winner = self.field.check_winner
                print(self.players[0].name+" ",self.field,self.players[1].name)
                self.field.give_to_pot(self.pot)
                if winner == 0 or winner == 1

    def win():
        print("wins")

    def war(self,pot):
        for i in range(3):
            self.give(self.cards[0],pot)


        def  play(self):
            top_card = self.cards[0]
            self.give(top_card,hand)

        def deal(self, hands, per_hand=26):
            for rounds in range(per_hand):
                for hand in hands:
                    if self.cards:
                        top_card = self.cards[0]
                        self.give(top_card, hand)
                    else:
                        print("Can't continue to deal. Out of cards!")

class War_Field(War_hand):

    @property
    def check_winner(self):
        if self.cards[0].value > self.cards[1].value:
            winner= 0
        elif self.cards[0].value < self.cards[1].value:
            winner = 1
        else:
            winner = "war"
        return winner
    def give_to_pot(self,pot):
        for i in range(len(self.cards)):
            self.give(self.cards[0],pot)

class War_Pot(War_hand):
    def give_to_winner(self,winner):
        for i in range(len(self.cards)):
            self.give(self.cards[0],winner)

    def main():
        names = []
        game = War_game


        










                
