from banking_pkg import account

def atm_menu(name):
    print("")
    print("          === Automated Teller Machine ===          ")
    print("User: " + name)
    print("------------------------------------------")
    print("| 1.    Balance     | 2.    Deposit      |")
    print("------------------------------------------")
    print("------------------------------------------")
    print("| 3.    Withdraw    | 4.    Logout       |")
    print("------------------------------------------")

print("          === Automated Teller Machine ===          ")


name = input("Enter name to register: ")
pin = input("Enter PIN: ")
balance = 0
counter = 0

print(f"{name} has been registered with a starting balance of ${balance}")

while counter < 3:
    print("\n          === Automated Teller Machine ===          ")
    name_to_validate = input("Enter name: ")
    pin_to_validate = input("Enter PIN: ")
    if name_to_validate == name and pin_to_validate == pin:
        print("Login successful!")
        break
    else:
        counter+=1
        print("you have 3 attempts before we lock your account.")
        if counter == 1:
            print(f"Invalid credentials!")
            print(f"this is your {counter} attempt")
        elif counter == 2:
            print(f"Invalid credentials!")
            print(f"this is your {counter} attempt")
            print("\nThis is your FINAL attempt...")
        else:
            if counter == 3:
                print("your account has been locked...")
                print("Please call the customer service...")
                print("Goodbye!")
                exit()
while True:
    atm_menu(name)
    option = input("Choose an option: ")
    if option == "1":
        print(f"Current balance ${account.show_balance(balance)}")
    elif option == "2":
        add_balance = account.deposit(balance)
        balance = add_balance 
        print(f"Current Balance ${balance}")
    elif option == "3":
        subtract_balance = account.withdraw(balance)
        balance = subtract_balance
        print(f"Current Balance ${balance}")
    else:
        if option == "4":
            print(f"Goodbye {account.logout(name)}!")
        exit()


    









