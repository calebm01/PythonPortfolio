
def input1(num1, num2):
    num1 = int(input("input first number "))
    num2 = int(input("input second number "))
    function = input("Please type in the math operation you would like to complete: \n + for addition \n - for subtraction \n * for multiplication \n / for division (keep in mind num1 is the numerator and num2 is the denominator)")
    if function == "+":
        addition()
    elif function == "-":
        subtraction()
    elif function == "*":
        multiplication()
    elif function == "/":
        division()
    else:
        print("you have input an invalid function, please try again")
        main()

def addition(num1, num2):
    print(num1, '+', num2, '=')
    print(num1 + num2)

def subtraction(num1, num2):
    print(num1, "-", num2, "=")
    print(num1 - num2)

def multiplication(num1, num2):
    print(num1, "*", num2, "=")
    print(num1 * num2)

def division(num1, num2):
    if num2 == 0:
        print("Dividing by zero is impossible")
    else:
        print(num1, "/", num2, "=")
        print(num1 / num2)
        
def main():
    input1(num1, num2)
    addition(num1, num2)
    subtraction(num1, num2)
    multiplication(num1, num2)
    division(num1, num2)
    print(" ")

main()
