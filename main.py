from user import User
import re
import os.path
from os import path

pattern = '^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$'
email_valid = True


def main():
    
    if not os.path.exists('login_system/users'):
        os.mkdir('login_system/users')

    user_input = input("login, add, remove or edit: ").lower()

    if user_input == "login":
        login()
    elif user_input == "add":
        create_user()
    elif user_input == "remove" or user_input == "rm":
        remove_user()
    elif user_input == "edit":
        user_edit()

    

    
    
def create_user():
    username = input("Wpisz nazwę użytkownika: ")
    userpass = input("Wpisz hasło: ")
    useremail = input("Wpisz email: ")
    if not validate_email(useremail):
        print("Invalid email... retype")
        useremail = input("Wpisz email: ")

    name = User(username,userpass,useremail)

    if name.email == "":
        name.email = "None"

    print(f"Created new user: {name.name}")

    with open("login_system/users/" + name.name + ".txt", "w") as f:
        f.write(name.name)
        f.write("\n")
        f.write(name.password)
        f.write("\n")
        f.write(name.email)
    
def login():
    username_input = input("Wpisz nazwę użytkownika: ")
    while True:
        try:
            with open("login_system/users/" + username_input + ".txt", "r") as f:
                user_file = f.readlines()
            userpassword_input = input("Password: ")
            if username_input == user_file[0].replace("\n", "") and userpassword_input == user_file[1].replace("\n", ""):
                print("Login succesful...\n")
            else:
                print("Something went wrong")
                print("Name-input : "+username_input + " | "+ "Name-file: " + user_file[0])
                print("Password-input : "+userpassword_input + " | "+ "pass-file: " + user_file[1])
        except:
            print("User not found in database")
            break
        
def remove_user():
    
    return
def user_edit():
    return

def validate_email(email):
    global email_valid
    if re.search(pattern, email):
        email_valid = True
    else:
        email_valid = False

    return

main()