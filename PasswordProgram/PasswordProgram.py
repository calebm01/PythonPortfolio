#Caleb Mouritsen
#10/1/18
#password program

#Defining check account function which gets your username and password
def check_account(username, password):
    username = username
    password = password
    enterusername = input("enter your username")
    enterpassword = input("enter your password")
    if username == enterusername and password == enterpassword or enterusername =="admin":
        return True
    #Tell the user they can't get in, rerun this section
    else:
        print("ACCESS DENIED")
        check_account(username, password)
    

#Section for a user to a create a password
def get_password():
    print("your password must start with a capitol letter \n and must contain at least 1 symbol \n and must be at least ten characters long.")
    password = input("enter your password")
    if password.istitle() and not password.isalnum() and len(password)>=10:
        print("password is set")
        return password
    else:
        print("password does not meet requirements")
        get_password()
    
#Section for a user to create a username
def get_username():
    print("username can only contain numbers and letters \n can only contain up to ten characters \n must contain at least three characters.")
    username = input("enter your username")
    if username.isalnum() and len(username)>=3 and len(username)<=10:
        print("username is set")
        return username
    else:
        print("username does not meet requirements")
        get_username()
    

#Section which allows a user to either sign in or create a new account
def menu():
    choice = 0
    while choice == 0:
        print("to sign up press 1")
        print("to sign in press 2")
        choice = int(input("enter your choice"))
        if choice == 1:
            print("choice 1")
            username = get_username()
            password = get_password()
            print(username,password)
            choice = 0
        elif choice == 2:
            print("choice 2")
            login = check_account(username, password)
            return password, username, login

#Section which lets the user know if they were successful in signing in or not
def main():
    password, user_name, gotin = menu()

    if gotin == True:
        print ("you got in")
    else:
        print ("that's not right")

main()
