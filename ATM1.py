# ============================================
#          ATM MACHINE - PYTHON
#       WITHOUT FUNCTIONS / CLASSES
# ============================================

from datetime import datetime

# Account details
account_number = "1234567890"
account_holder = "Harshal Badgujar"
pin = "1234"
balance = 25000

# Daily withdrawal limit
daily_limit = 20000
withdrawn_today = 0

# Transaction history
transactions = []

# Add initial transaction
transactions.append({
    "date": datetime.now().strftime("%d-%m-%Y"),
    "type": "Saving",
    "amount": 25000,
    "balance": balance
})


print("========================================")
print("          WELCOME TO PYTHON ATM")
print("========================================")


# ============================================
#              PIN LOGIN
# ============================================

attempts = 0
login_success = False

while attempts < 3:

    entered_pin = input("Enter your 4-digit PIN: ")

    if entered_pin == pin:
        login_success = True
        print("\nLogin Successful!")
        print("Welcome,", account_holder)
        break

    else:
        attempts += 1
        print("Incorrect PIN.")

        if attempts < 3:
            print("Attempts remaining:", 3 - attempts)

if login_success == False:

    print("\nYour account has been blocked.")
    print("Please try again later.")

else:

    # ============================================
    #              ATM MENU
    # ============================================

    while True:

        print("\n========================================")
        print("              ATM MENU")
        print("========================================")
        print("1. Check Balance")
        print("2. Withdraw Money")
        print("3. Deposit Money")
        print("4. Fast Cash")
        print("5. Money Transfer")
        print("6. Mini Statement")
        print("7. Account Details")
        print("8. Change PIN")
        print("9. Withdrawal Limit")
        print("10. Logout")
        print("11. Exit")
        print("========================================")

        choice = input("Enter your choice: ")


        # ========================================
        #           1. CHECK BALANCE
        # ========================================

        if choice == "1":

            print("\n--------------------------------")
            print("         CHECK BALANCE")
            print("--------------------------------")

            print("Account Holder :", account_holder)
            print("Available Balance : ₹", balance)


        # ========================================
        #           2. WITHDRAW MONEY
        # ========================================

        elif choice == "2":

            print("\n--------------------------------")
            print("          WITHDRAW MONEY")
            print("--------------------------------")

            amount = input("Enter amount: ₹")

            if amount.isdigit():

                amount = int(amount)

                if amount <= 0:
                    print("Invalid amount.")

                elif amount % 100 != 0:
                    print("Amount must be in multiples of ₹100.")

                elif amount > balance:
                    print("Insufficient balance.")

                elif withdrawn_today + amount > daily_limit:
                    print("Daily withdrawal limit exceeded.")

                else:

                    balance = balance - amount
                    withdrawn_today = withdrawn_today + amount

                    transactions.append({
                        "date": datetime.now().strftime("%d-%m-%Y"),
                        "type": "Withdrawal",
                        "amount": amount,
                        "balance": balance
                    })

                    print("\nPlease collect your cash.")
                    print("Withdrawn Amount : ₹", amount)
                    print("Remaining Balance : ₹", balance)

            else:
                print("Please enter a valid number.")


        # ========================================
        #           3. DEPOSIT MONEY
        # ========================================

        elif choice == "3":

            print("\n--------------------------------")
            print("           DEPOSIT MONEY")
            print("--------------------------------")

            amount = input("Enter amount: ₹")

            if amount.isdigit():

                amount = int(amount)

                if amount <= 0:

                    print("Invalid amount.")

                else:

                    balance = balance + amount

                    transactions.append({
                        "date": datetime.now().strftime("%d-%m-%Y"),
                        "type": "Deposit",
                        "amount": amount,
                        "balance": balance
                    })

                    print("\nMoney deposited successfully.")
                    print("Deposited Amount : ₹", amount)
                    print("New Balance : ₹", balance)

            else:
                print("Please enter a valid number.")


        # ========================================
        #           4. FAST CASH
        # ========================================

        elif choice == "4":

            print("\n--------------------------------")
            print("             FAST CASH")
            print("--------------------------------")

            print("1. ₹500")
            print("2. ₹1000")
            print("3. ₹2000")
            print("4. ₹5000")
            print("5. ₹10000")
            print("6. Cancel")

            fast_choice = input("Select option: ")

            if fast_choice == "1":
                amount = 500

            elif fast_choice == "2":
                amount = 1000

            elif fast_choice == "3":
                amount = 2000

            elif fast_choice == "4":
                amount = 5000

            elif fast_choice == "5":
                amount = 10000

            elif fast_choice == "6":
                print("Fast cash cancelled.")
                continue

            else:
                print("Invalid option.")
                continue


            if amount > balance:

                print("Insufficient balance.")

            elif withdrawn_today + amount > daily_limit:

                print("Daily withdrawal limit exceeded.")

            else:

                balance = balance - amount
                withdrawn_today = withdrawn_today + amount

                transactions.append({
                    "date": datetime.now().strftime("%d-%m-%Y"),
                    "type": "Fast Cash",
                    "amount": amount,
                    "balance": balance
                })

                print("\nPlease collect your cash.")
                print("Withdrawn Amount : ₹", amount)
                print("Remaining Balance : ₹", balance)


        # ========================================
        #           5. MONEY TRANSFER
        # ========================================

        elif choice == "5":

            print("\n--------------------------------")
            print("           MONEY TRANSFER")
            print("--------------------------------")

            receiver = input("Enter receiver account number: ")

            if len(receiver) != 10 or not receiver.isdigit():

                print("Invalid account number.")

            elif receiver == account_number:

                print("You cannot transfer money to yourself.")

            else:

                amount = input("Enter transfer amount: ₹")

                if amount.isdigit():

                    amount = int(amount)

                    if amount <= 0:

                        print("Invalid amount.")

                    elif amount > balance:

                        print("Insufficient balance.")

                    else:

                        confirm = input(
                            "Confirm transfer? (Y/N): "
                        ).upper()

                        if confirm == "Y":

                            balance = balance - amount

                            transactions.append({
                                "date": datetime.now().strftime("%d-%m-%Y"),
                                "type": "Money Transfer",
                                "amount": amount,
                                "balance": balance
                            })

                            print("\nTransfer successful.")
                            print("Transferred : ₹", amount)
                            print("Remaining Balance : ₹", balance)

                        else:

                            print("Transfer cancelled.")

                else:

                    print("Invalid amount.")


        # ========================================
        #           6. MINI STATEMENT
        # ========================================

        elif choice == "6":

            print("\n======================================================")
            print("                 MINI STATEMENT")
            print("======================================================")

            print("Account Holder :", account_holder)
            print("Account Number : ******" + account_number[-4:])

            print("------------------------------------------------------")

            for transaction in transactions:

                print(
                    transaction["date"],
                    "|",
                    transaction["type"],
                    "| ₹",
                    transaction["amount"],
                    "| Balance: ₹",
                    transaction["balance"]
                )

            print("------------------------------------------------------")


        # ========================================
        #           7. ACCOUNT DETAILS
        # ========================================

        elif choice == "7":

            print("\n--------------------------------")
            print("          ACCOUNT DETAILS")
            print("--------------------------------")

            print("Account Holder :", account_holder)
            print("Account Number : ******" + account_number[-4:])
            print("Balance        : ₹", balance)


        # ========================================
        #           8. CHANGE PIN
        # ========================================

        elif choice == "8":

            print("\n--------------------------------")
            print("             CHANGE PIN")
            print("--------------------------------")

            old_pin = input("Enter old PIN: ")

            if old_pin == pin:

                new_pin = input("Enter new 4-digit PIN: ")

                if len(new_pin) == 4 and new_pin.isdigit():

                    confirm_pin = input(
                        "Confirm new PIN: "
                    )

                    if new_pin == confirm_pin:

                        if new_pin == pin:

                            print(
                                "New PIN cannot be same as old PIN."
                            )

                        else:

                            pin = new_pin

                            print(
                                "PIN changed successfully."
                            )

                    else:

                        print("PIN confirmation doesn't match.")

                else:

                    print("PIN must contain exactly 4 digits.")

            else:

                print("Incorrect old PIN.")


        # ========================================
        #           9. WITHDRAWAL LIMIT
        # ========================================

        elif choice == "9":

            print("\n--------------------------------")
            print("        WITHDRAWAL LIMIT")
            print("--------------------------------")

            remaining_limit = daily_limit - withdrawn_today

            print("Daily Limit       : ₹", daily_limit)
            print("Withdrawn Today   : ₹", withdrawn_today)
            print("Remaining Limit   : ₹", remaining_limit)


        # ========================================
        #           10. LOGOUT
        # ========================================

        elif choice == "10":

            print("\nYou have been logged out.")
            print("Thank you for using Python ATM.")

            break


        # ========================================
        #           11. EXIT
        # ========================================

        elif choice == "11":

            print("\nThank you for using Python ATM.")
            print("Have a nice day!")

            break


        # ========================================
        #           INVALID CHOICE
        # ========================================

        else:

            print("\nInvalid choice.")
            print("Please select a valid option.")