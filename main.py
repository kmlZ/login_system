from user import User
import re
import os.path
from os import path

pattern = re.compile("[a-zA-z0-9]+\@[a-zA-Z0-9]+\.[a-zA-Z]+")

email_valid = True
is_logged_in = False
is_logged_in_as_root = False
current_user_name = ""
current_user_password = ""
user_to_remove = ""


def main():
    
    if not os.path.exists('login_system/users'):
        os.mkdir('login_system/users')
    
    if not os.path.exists('login_system/users/root.txt'):
        print("Create root account \n")
        create_root()

    user_input = input("login, add, remove or edit: ").lower()

    if user_input == "login":
        username_input = input("Type username: ")
        password_input = input("Type password: ")       
        login(username_input, password_input)
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
        f.write("\n")
        f.write("guest")
    main()
    
def login(username, password):
    global is_logged_in
    global is_logged_in_as_root
    global current_user_name
    global current_user_password
    while True:
        try:
            with open("login_system/users/" + username + ".txt", "r") as f:
                user_file = f.readlines()                
            if username == user_file[0].replace("\n", "") and password == user_file[1].replace("\n", ""):
                print("Login succesful...\n")
                is_logged_in = True
                current_user_name = user_file[0].replace("\n", "") 
                current_user_password = user_file[1].replace("\n", "")
                if user_file[3].replace("\n", "") == "root":
                    is_logged_in_as_root = True
                else:
                    is_logged_in_as_root = False
                main()
        except Exception as error:
            print("User not found in database")
            print(str(error))           
            break
        
def remove_user():
    global user_to_remove

    user_to_remove = input("Wpisz nazwę użytkownika do usunięcia: ")
    if is_logged_in_as_root == True and current_user_name != user_to_remove:
        os.remove("login_system/users/" + user_to_remove + ".txt")
        main()
    elif is_logged_in_as_root != True :
        print("You aren't allowed to remove user. Log in as root")
        root_input = input("Type root account username: ")
        root_input_passwd = input("Type root accoutn password: ")
        login(root_input, root_input_passwd)
    

    
    
def user_edit():
    return



def create_root():
    name = input("Type root accoutn name: ")
    passwd = input("Type password: ")
    root_email = input("Type email: ")
    while not validate_email(root_email):
        print("Invalid email... retype")
        print(root_email)
        root_email = input("Type email: ")
    root = User(name, passwd, root_email)
    try:
        with open(f"login_system/users/{root.name}.txt", "w") as root_file:
            root_file.write(root.name)
            root_file.write("\n")
            root_file.write(root.password)
            root_file.write("\n")
            root_file.write(root.email)
    except:
        print("Something went wrong in create_root() function")

    if len(root.password) < 3:
        print("Password too short.")
        main()

     
def validate_email(email):
    if re.search(pattern, email):
        return True
    else:
        return False

    

main()