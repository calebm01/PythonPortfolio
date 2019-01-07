#Caleb Mouritsen
#12/10/18
#Tic-Tac-Toe Game against a computer opponent

X = "x"
O = "O"
EMPTY = " "
TIE = "TIE"
NUM_SQUARES = 9

#first function, displays menu
def display_instructions():
    print("welcome to Tic-Tac-toe!\n")
    print("\nYou're probably garbage at Tic-Tac-Toe")

    choice = input("Press 1 to play Tic-Tac-Toe. \n Press 2 to quit \n Press 3 for instructions")
    
    while True:
        if choice == "1":
            print("game placeholder")
            break
            
        elif choice == "2":
            print("Wow you're scared to play me huh")
            break
        
        elif choice == "3":
            print(""" Welcome to the greatest intellectual challenge of all time: Tic-Tac-Toe. You'll be playing the computer.
        You will utilize index positioning to make your moves, input 0-8 to put your piece in a specific position
        The board is as shown



                      0 | 1 | 2
                      ---------
                      3 | 4 | 5
                      ---------
                      6 | 7 | 8


                      """)
            print("\n index positions start at 0 for coding convenience")
            print("\nreturning to menu...\n")
            display_instructions()
                  
        else:
            print("That's not an available choice")

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

def pieces():
    #Determine if the player goes first
    player = None
    computer = None
    go_first = ask_yes_no("Do you want to go first? (y/n):")
    if go_first == "y":
        print("Going first is for losers")
        player = X
        computer = O
    else:
        print("Going second is cowardly")
        computer = X
        player = O
    return computer, player

#Building a new board
def new_board():
    board = []
    for square in range(NUM_SQUARES):
        board.append(EMPTY)
    return board

#Displaying the board
def display_board(board):
    print("\n\t", board[0], "|", board[1], "|", board[2])
    print("\t", "---------")
    print("\t", board[3], "|", board[4], "|", board[5])
    print("\t", "---------")
    print("\t", board[6], "|", board[7], "|", board[8], "\n")

def legal_move(board):
    #Defining what is a legal move in our Tic-Tac-Toe game
    #Determine where on our board moves can be made
    moves = []
    for square in range(len(board)):
        if board[square] == EMPTY:
            moves.append(square)
    return moves

def winner(board):
    #Setting up what the board needs to look like in order to win
    ways_to_win = ((0, 1, 2),
                   (3, 4, 5),
                   (6, 7, 8),
                   (0, 3, 6),
                   (1, 4, 7),
                   (2, 5, 8),
                   (0, 4, 8),
                   (2, 4, 6))
    for row in ways_to_win:
        if board[row[0]] == board[row[1]] == board[row[2]] != EMPTY:
            winner = board[row[0]]
            return winner

    if EMPTY not in board:
        return TIE
    
    return None


def human_move(board, player):
    #Get human move. Check if human move is legal
    legal = legal_move(board) 
    move = None
    while move not in legal:
        move = ask_num("Where will you move? (0-8):", 0, NUM_SQUARES)
        if move not in legal:
            print("Trying to cheat?, try again\n")
        
        print("ok")
        return move
        
    
def next_turn(turn):
    #Switch turns
    if turn == X:
        return O
    else:
        return X

def computer_move(board, computer, player):
    #Make computer move
    #Make a copy of the board since function will be changing list
    board = board[:]
    #The best positions to have in order
    best_moves = (4, 0, 2, 6, 8, 1, 3, 5, 7)
    print("I'm gonna take square number", end=" ")
    #If computer can win, it will take that move
    for move in legal_move(board):
        board[move] = computer
        if winner(board) == computer:
            print(move)
            return move
        #undo move
        board[move] = EMPTY
    #If human can win, block that move
    for move in legal_move(board):
        board[move] = player
        if winner(board) == player:
            print(move)
            return move
        #undo move
        board[move] = EMPTY

    #since no one can win on next move, pick best open square
    for move in best_moves:
        if move in legal_move(board):
            print(move)
            return move
    

def congrat_winner(the_winner, computer, player):
    #Outputting the result of the game
    if the_winner != TIE:
        print(the_winner,"won\n")
    else:
        print("A tie? I'll consider that a win because of your inferior intellect")
    if the_winner == player:
            print("You beat me")
    elif the_winner == computer:
            print("You lose, loser")
   


    
def main():
    display_instructions()

    computer, player = pieces()

    turn = X

    board = new_board()

    display_board(board)

    while not winner(board):
        

        if turn == player:
            move = human_move(board, player)
            board[move] = player
        else:
            move = computer_move(board, computer, player)
            board[move] = computer
        display_board(board)
        turn = next_turn(turn)

    the_winner = winner(board)

    congrat_winner(the_winner, computer,player)

main()

