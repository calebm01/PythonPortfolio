#Caleb Mouritsen
# 10/24/18
# Name and age checking program

#Prompt user input for name and age
name = input("what is your name")
age = input("what is your age")

#Use multiple "and" statements and "or" statements to determine if the condition is met
if name.isalpha() and name.istitle() and age.isdigit() and age<"25" or name == "Balthazar, immune to blade and arrow":
    print("The name you entered was:", name + ",", "your age was", age)
#If the condition isn't met
else
    print("Sorry, you aren't cool enough")
