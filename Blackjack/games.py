#Caleb Mouritsen
#2/13/19
#Games

import Card

def ask_yes_no(question):
    #Recallable yes or no question function, will be used on every yes or no question
    response = None
    while response not in ("y", "yes", "no", "n"):
        response = input(question).lower()
    return response

def ask_num(question, low, high):
    #Function looking to determine numbers, ask for user input
    response = "9999"
    while True:
        if response.isdigit():
            if int(response) in range(low,high):
                break
            else:
                response = input(question)
        else:
            print("you must enter a number")
            response = input(question)
    return int(response)




def next_turn(turn):
    #Switch turns
    if turn == X:
        return O
    else:
        return X

def flip_a_coin():
    import random
    #randomizing the coin toss
    coin = ["Heads", "Tails"]
    side = random.choice(coin)

def roll(self):
    """This function imports random, and then asks for a random number between 1 and 6 from the computer.
         The computer will then tell the user what their number is from the dice"""
    import random
    die1 = random.randint(1,6)
    print("you rolled a", die1)
    roll = die1
    return roll

def winner_grats():
    """This function simply displays a congratulations message to the player once the win condition is met"""
    print("congratulations, you won")

def add_to_score(score,points):
    """Adds points to an earned score"""
    new_score = score
    score += points
    return new_score

class Player(object):
    def __init__(self, name):
        self.name = name
        self.score = score

    def __str__(self):
        rep = self.name
        rep = rep +" " + str(self.score)
        return rep


if __name__== "__main__":
    print("You ran this module directly (and did not import it)")
    input("\n\nPress the enter key to exit.")
