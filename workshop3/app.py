from donations_pkg.homepage import *
from donations_pkg.user import *


import sys

# TASK 2
database = {"admin": "password123", "ntorres": "pw"}
donations = []
authorized_user = ""

# To make finding a dictionaries value dynamic
# user = "ntorres"
# database[user]

while True:
    # What goes into a while loop is what you want to keep seeing
    show_homepage()
    if len(authorized_user) == 0:
        print("You must be logged in to donate")
    else:
        print(f"Logged in as: {authorized_user}")


# TASK 3- Handle user input
    user_option = int(input("Choose an option: "))
    if user_option == 1:
        username = input("Enter username: ")
        password = input("Enter password: ")
        authorized_user = login(database, username, password)
    elif user_option == 2:
        username = input("Enter username: ")
        password = input("Enter password: ")
        authorized_user = register(database, username)
        if len(authorized_user) != 0:
            # if database not empty then add the new key and password to dict
            database[username] = password
    elif user_option == 3:
        # TASK 3 NOT WORKING CORRECTLY--------
        if len(authorized_user) == 0:
            print("You are not logged in.")
        else:
            donation_string = donate(authorized_user)
            donations.append(donation_string)
    elif user_option == 4:
        show_donations(donations)
    elif user_option == 5:
        print(f"Goodbye, {authorized_user}")
        sys.exit()  # break
    else:
        continue


# QUESTIONS:
# When would you use the TRY Except
