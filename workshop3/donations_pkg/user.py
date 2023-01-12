# TASK 4 - Login Functionality

def login(database, username, password):
    # database will be a dictionary
    # username/ password willl contain strings
    if username in database.keys():  # if the key is in the database dictionary
        # if the value of username key is in the database dictionary
        if password in database.values():
            # if password == database[username]:
            print(f"Welcome, {username}!")
            return username
    elif username in database:  # looking for a key in a database
        # checking that the password isn't in the values
        if password != database[username]:
            print("Incorrect password for admin!")
    else:
        print("Username and password does not exist.")
    return ""  # an empty string


# TASK 5 Register functionality
def register(database, username):
    if username in database:
        print("Username already registered")
        return ""
    else:
        print(f"{username}'s sign in is successful!")
        return username
