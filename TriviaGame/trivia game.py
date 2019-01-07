#Caleb Mouritsen
#1/19
#Trivia Challenge
# Trivia Game that reads a plain text file

import sys

def open_file(file_name,mode):
    #Open a file
    try:
        the_file = open(file_name,mode)
    except IOError as e:
        print("Unbale to open the file", file_name, "Ending program.\n", e)
        input("\n\nPress any key to exit.")
        sys.exit()
    else:
        return the_file


def next_line(the_file):
    #Return next line from the trivia file, formatted.
    line = the_file.readline()
    line = line.replace("\\","\n")
    return line

def next_block(the_file):
    #Function to get a category, its question, its answers, correct answer
    #And explanation
    category = next_line(the_file)
    
    question = next_line(the_file)

    answer_list = []
    for i in range(4):
        answer_list.append(next_line(the_file))
        
    correct = next_line(the_file)
    if correct:
        correct = correct[0]

    explanation = next_line(the_file)

    return category, question, answer_list, correct, explanation

def welcome(title):
    #Function to display a welcome message
    print("\t\tWelcome to the trivia challenge!\n")
    print("\t\t", title, "\n")
    
def main():
    #Main method
    the_file = open_file("test_file.txt","r")
    title = next_line(the_file)
    welcome(title)
    score = 0
    
    category, question, answer_list, correct, explanation = next_block(the_file)
    
    while category:
        print(category)
        print(question)
        for i in range(4):
            print(answer_list[i])
        user_answer = input("What is the answer?")
        if user_answer == correct:
            print("You got it!")
            score += 1
            print(explanation)
            print(score)
        else:
            print("incorrect")
            print(explanation)
            print(score)

        category, question, answer_list, correct, explanation = next_block(the_file)

    
    print("\nThanks for playing!")
    print("Your final score:", score)

main()
    
        
         


