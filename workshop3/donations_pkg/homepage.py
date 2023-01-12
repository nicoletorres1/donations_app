

def show_homepage():
    print("")
    print("       === DonateMe Homepage ===          ")
    print("------------------------------------------")
    print("| 1.    Login     | 2.    Register       |")
    print("------------------------------------------")
    print("| 3.    Donate    | 4.    Show Donations |")
    print("------------------------------------------")
    print("|              5. Exit                   |")
    print("------------------------------------------")


def donate(username):
    donation_amt = float(input("Enter amount to donate: "))
    donation_string = f"User: {username} donated {donation_amt:.2f}"
    print("Thank you for your donation!", donation_string)
    return donation_string


def show_donations(donations):
    print("\n--- All Donations ---")
    if len(donations) == 0:
        print("Currently, there are no donations.")
    else:
        for i in donations:
            print(i)

    # Format string to have two decimals
    # f-string: print(f"Your balance is: ${balance:.2f}"
    # replace balance variable inside the {} with variable you need
