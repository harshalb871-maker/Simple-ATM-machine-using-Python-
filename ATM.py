# ============================================================
#                 ATM MACHINE - PYTHON PROJECT
# ============================================================

from datetime import datetime


# ------------------------------------------------------------
# ATM CLASS
# ------------------------------------------------------------

class ATM:
    def __init__(self):
        # Sample account data
        self.account = {
            "account_number": "1234567890",
            "name": "Harshal Badgujar",
            "pin": "1234",
            "balance": 25000.00,
            "mobile": "9876543210"
        }

        # Transaction history
        self.transactions = []

        # ATM rules
        self.daily_withdrawal_limit = 20000
        self.withdrawn_today = 0

        # Add initial transaction
        self.add_transaction(
            "ACCOUNT OPENING",
            25000.00,
            25000.00
        )

    # --------------------------------------------------------
    # TRANSACTION HISTORY
    # --------------------------------------------------------

    def add_transaction(self, transaction_type, amount, balance):
        transaction = {
            "date": datetime.now().strftime("%d-%m-%Y"),
            "time": datetime.now().strftime("%H:%M:%S"),
            "type": transaction_type,
            "amount": amount,
            "balance": balance
        }

        self.transactions.append(transaction)

    # --------------------------------------------------------
    # PIN LOGIN
    # --------------------------------------------------------

    def login(self):
        attempts = 3

        while attempts > 0:
            pin = input("Enter your 4-digit PIN: ")

            if pin == self.account["pin"]:
                print("\nLogin successful!")
                print(f"Welcome, {self.account['name']}")
                return True

            attempts -= 1

            if attempts > 0:
                print(f"Incorrect PIN. {attempts} attempt(s) remaining.\n")
            else:
                print("\nToo many incorrect attempts.")
                print("Your account has been temporarily blocked.")

        return False

    # --------------------------------------------------------
    # CHECK BALANCE
    # --------------------------------------------------------

    def check_balance(self):
        print("\n--------------------------------")
        print("          ACCOUNT BALANCE")
        print("--------------------------------")
        print(f"Available Balance : ₹{self.account['balance']:.2f}")
        print("--------------------------------")

    # --------------------------------------------------------
    # DEPOSIT
    # --------------------------------------------------------

    def deposit(self):
        print("\n--------------------------------")
        print("             DEPOSIT")
        print("--------------------------------")

        try:
            amount = float(input("Enter amount to deposit: ₹"))

            if amount <= 0:
                print("Amount must be greater than ₹0.")
                return

            self.account["balance"] += amount

            self.add_transaction(
                "DEPOSIT",
                amount,
                self.account["balance"]
            )

            print(f"\n₹{amount:.2f} deposited successfully.")
            print(f"New Balance: ₹{self.account['balance']:.2f}")

        except ValueError:
            print("Invalid amount. Please enter a number.")

    # --------------------------------------------------------
    # WITHDRAW
    # --------------------------------------------------------

    def withdraw(self):
        print("\n--------------------------------")
        print("            WITHDRAW")
        print("--------------------------------")

        try:
            amount = float(input("Enter amount to withdraw: ₹"))

            if amount <= 0:
                print("Amount must be greater than ₹0.")
                return

            # Check balance
            if amount > self.account["balance"]:
                print("\nInsufficient balance.")
                print(f"Available Balance: ₹{self.account['balance']:.2f}")
                return

            # Check daily limit
            if self.withdrawn_today + amount > self.daily_withdrawal_limit:
                remaining = (
                    self.daily_withdrawal_limit -
                    self.withdrawn_today
                )

                print("\nDaily withdrawal limit exceeded.")
                print(f"Remaining withdrawal limit: ₹{remaining:.2f}")
                return

            # ATM usually dispenses multiples of 100
            if amount % 100 != 0:
                print("\nPlease enter amount in multiples of ₹100.")
                return

            self.account["balance"] -= amount
            self.withdrawn_today += amount

            self.add_transaction(
                "WITHDRAW",
                amount,
                self.account["balance"]
            )

            print(f"\nPlease collect your cash: ₹{amount:.2f}")
            print(f"Remaining Balance: ₹{self.account['balance']:.2f}")

        except ValueError:
            print("Invalid amount. Please enter a number.")

    # --------------------------------------------------------
    # FAST CASH
    # --------------------------------------------------------

    def fast_cash(self):
        print("\n--------------------------------")
        print("             FAST CASH")
        print("--------------------------------")

        options = [500, 1000, 2000, 5000, 10000]

        for i, amount in enumerate(options, 1):
            print(f"{i}. ₹{amount}")

        print("6. Cancel")

        choice = input("\nSelect option: ")

        if choice == "6":
            print("Fast Cash cancelled.")
            return

        if choice not in ["1", "2", "3", "4", "5"]:
            print("Invalid option.")
            return

        amount = options[int(choice) - 1]

        if amount > self.account["balance"]:
            print("Insufficient balance.")
            return

        if self.withdrawn_today + amount > self.daily_withdrawal_limit:
            print("Daily withdrawal limit exceeded.")
            return

        self.account["balance"] -= amount
        self.withdrawn_today += amount

        self.add_transaction(
            "FAST CASH",
            amount,
            self.account["balance"]
        )

        print(f"\nPlease collect your cash: ₹{amount:.2f}")
        print(f"Remaining Balance: ₹{self.account['balance']:.2f}")

    # --------------------------------------------------------
    # CHANGE PIN
    # --------------------------------------------------------

    def change_pin(self):
        print("\n--------------------------------")
        print("            CHANGE PIN")
        print("--------------------------------")

        old_pin = input("Enter current PIN: ")

        if old_pin != self.account["pin"]:
            print("Incorrect current PIN.")
            return

        new_pin = input("Enter new 4-digit PIN: ")

        if len(new_pin) != 4 or not new_pin.isdigit():
            print("PIN must contain exactly 4 digits.")
            return

        confirm_pin = input("Confirm new PIN: ")

        if new_pin != confirm_pin:
            print("PIN confirmation does not match.")
            return

        if new_pin == old_pin:
            print("New PIN cannot be the same as old PIN.")
            return

        self.account["pin"] = new_pin

        print("\nPIN changed successfully.")

    # --------------------------------------------------------
    # MINI STATEMENT
    # --------------------------------------------------------

    def mini_statement(self):
        print("\n==========================================================")
        print("                    MINI STATEMENT")
        print("==========================================================")

        print(f"Account Holder : {self.account['name']}")
        print(
            f"Account Number : ****"
            f"{self.account['account_number'][-4:]}"
        )

        print("----------------------------------------------------------")
        print(
            f"{'Date':<12}"
            f"{'Time':<10}"
            f"{'Transaction':<18}"
            f"{'Amount':>12}"
            f"{'Balance':>15}"
        )
        print("----------------------------------------------------------")

        # Show last 10 transactions
        for transaction in self.transactions[-10:]:
            print(
                f"{transaction['date']:<12}"
                f"{transaction['time']:<10}"
                f"{transaction['type']:<18}"
                f"₹{transaction['amount']:>10.2f}"
                f"₹{transaction['balance']:>13.2f}"
            )

        print("----------------------------------------------------------")

    # --------------------------------------------------------
    # TRANSFER MONEY
    # --------------------------------------------------------

    def transfer_money(self):
        print("\n--------------------------------")
        print("          MONEY TRANSFER")
        print("--------------------------------")

        receiver = input("Enter receiver account number: ")

        if not receiver.isdigit() or len(receiver) != 10:
            print("Invalid account number.")
            return

        if receiver == self.account["account_number"]:
            print("You cannot transfer money to your own account.")
            return

        try:
            amount = float(input("Enter transfer amount: ₹"))

            if amount <= 0:
                print("Amount must be greater than ₹0.")
                return

            if amount > self.account["balance"]:
                print("Insufficient balance.")
                return

            confirmation = input(
                f"Transfer ₹{amount:.2f} to account "
                f"XXXXXX{receiver[-4:]}? (Y/N): "
            ).upper()

            if confirmation != "Y":
                print("Transfer cancelled.")
                return

            self.account["balance"] -= amount

            self.add_transaction(
                "MONEY TRANSFER",
                amount,
                self.account["balance"]
            )

            print("\nTransfer successful.")
            print(f"Transferred Amount: ₹{amount:.2f}")
            print(f"Remaining Balance: ₹{self.account['balance']:.2f}")

        except ValueError:
            print("Invalid amount.")

    # --------------------------------------------------------
    # ACCOUNT DETAILS
    # --------------------------------------------------------

    def account_details(self):
        print("\n--------------------------------")
        print("         ACCOUNT DETAILS")
        print("--------------------------------")

        print(f"Name           : {self.account['name']}")

        print(
            "Account Number : "
            f"{'*' * 6}{self.account['account_number'][-4:]}"
        )

        print(
            "Mobile Number  : "
            f"{'*' * 6}{self.account['mobile'][-4:]}"
        )

        print(f"Balance        : ₹{self.account['balance']:.2f}")

        print("--------------------------------")

    # --------------------------------------------------------
    # WITHDRAWAL LIMIT
    # --------------------------------------------------------

    def withdrawal_limit(self):
        print("\n--------------------------------")
        print("       WITHDRAWAL LIMIT")
        print("--------------------------------")

        remaining = (
            self.daily_withdrawal_limit -
            self.withdrawn_today
        )

        print(
            f"Daily Limit       : "
            f"₹{self.daily_withdrawal_limit:.2f}"
        )

        print(
            f"Withdrawn Today  : "
            f"₹{self.withdrawn_today:.2f}"
        )

        print(
            f"Remaining Limit  : "
            f"₹{remaining:.2f}"
        )

        print("--------------------------------")

    # --------------------------------------------------------
    # ATM MENU
    # --------------------------------------------------------

    def menu(self):

        while True:

            print("\n")
            print("================================================")
            print("                  ATM MACHINE")
            print("================================================")
            print("1.  Check Balance")
            print("2.  Withdraw Money")
            print("3.  Deposit Money")
            print("4.  Fast Cash")
            print("5.  Money Transfer")
            print("6.  Mini Statement")
            print("7.  Account Details")
            print("8.  Change PIN")
            print("9.  Withdrawal Limit")
            print("10. Logout")
            print("11. Exit")
            print("================================================")

            choice = input("Enter your choice: ")

            if choice == "1":
                self.check_balance()

            elif choice == "2":
                self.withdraw()

            elif choice == "3":
                self.deposit()

            elif choice == "4":
                self.fast_cash()

            elif choice == "5":
                self.transfer_money()

            elif choice == "6":
                self.mini_statement()

            elif choice == "7":
                self.account_details()

            elif choice == "8":
                self.change_pin()

            elif choice == "9":
                self.withdrawal_limit()

            elif choice == "10":
                print("\nYou have been successfully logged out.")
                break

            elif choice == "11":
                print("\nThank you for using our ATM.")
                return False

            else:
                print("\nInvalid choice. Please try again.")

        return True


# ------------------------------------------------------------
# MAIN PROGRAM
# ------------------------------------------------------------

def main():

    print("================================================")
    print("             WELCOME TO PYTHON ATM")
    print("================================================")

    atm = ATM()

    while True:

        if not atm.login():
            break

        continue_atm = atm.menu()

        if not continue_atm:
            break

        print("\nPlease insert your card again to login.")

    print("\n================================================")
    print("              THANK YOU!")
    print("================================================")


# ------------------------------------------------------------
# PROGRAM START
# ------------------------------------------------------------

if __name__ == "__main__":
    main()