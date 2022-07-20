account_name = "Joe"
account_balance = 100
account_password = "soup"

while True:
    print()
    print("Press b to get the balance")
    print("Press d to make a deposit")
    print("Press w to make a withdrawal")
    print("Press s to show the account")
    print("Press q to quit")
    print()

    action = input("What do you want to do? ").lower()[0]
    print()

    match action:
        case "b":
            print("Get Balance:")
            user_password = input("Please enter the password: ")
            if user_password != account_password:
                print("Incorrect password")
            else:
                print("Your balance is: ", account_balance)
        case "d":
            print("Deposit:")
            deposit_amount = int(input("Please enter amount to deposit: "))
            user_password = input("Please enter the password: ")

            if deposit_amount < 0:
                print("You cannot deposit a negative amount!")
            elif user_password != account_password:
                print("Incorrect password")
            else:
                account_balance += deposit_amount
                print("You new balance is:", account_balance)
        case "s":
            print("Show:")
            print("    Name", account_name)
            print("    Balance", account_balance)
            print("    Password", account_password)
            print()
        case "q":
            break
        case "w":
            print("Withdraw:")
            withdraw_amount = int(input("Please enter amount to withdraw: "))
            user_password = input("Please enter the password: ")

            if withdraw_amount < 0:
                print("You cannot withdraw a negative amount")
            elif user_password != account_password:
                print("Incorrect password for this account")
            elif withdraw_amount > account_balance:
                print("You cannot withdraw more than you have in your account")
            else:
                account_balance -= withdraw_amount
                print("Your new balance is:", account_balance)

print("Done")
