# Functions

def create_account():
    user = input("Enter a username: ")
    password = input("Enter a password: ")
    file = open('creds.txt', 'a')
    file.write(user)
    file.write(':')
    file.write(password)
    file.write('\n')
    print("User Created")
    return 

def login_to_account():
    file = open('creds.txt', 'r')
    text = file.read()
    user = input("Username: ")
    password = input("Password: ")
    if f'{user}:{password}' in text:
        print("Login successful")
    else:
        print('Incorrect username or password.')




Asking = input("Do you want to create a new account[enter 1 for creating account] or login to an existing accound[enter 2 for login to an existing account]: ")
if Asking == '1':
    print("Creating account")
    create_account()
elif Asking == '2':
    # user = login_to_account()
    print("Logging in to existing account")
    login_to_account()
else:
    print('Invalid Input')