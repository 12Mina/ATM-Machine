import time

#Class ATM: Encapsulates the functionalities of an ATM machine

class ATM:
    def __init__(self, initial_balance=1000000, initial_pin=123456789):
        self.balance = initial_balance
        self.pin = initial_pin
        self.transaction_history = []

# Checks if the entered PIN is correct.

    def validate_pin(self, input_pin):
        """Validate the entered PIN"""
        return input_pin == self.pin
    
 #Returns the current account balance

    def inquire_balance(self):
        """Return the current balance"""
        return self.balance
    
# Withdraws a specified amount from the account balance if funds are sufficient.

    def withdraw_cash(self, amount):
        """Withdraw cash from the account"""
        if amount <= self.balance:
            self.balance -= amount
            self.transaction_history.append(f"Withdrawn: {amount}")
            return amount
        else:
            return None
        
# Deposits a specified amount into the account.


    def deposit_cash(self, amount):
        """Deposit cash into the account"""
        self.balance += amount
        self.transaction_history.append(f"Deposited: {amount}")

#Changes the account PIN.

    def change_pin(self, new_pin):
        """Change the account PIN"""
        self.pin = new_pin
        self.transaction_history.append("PIN changed")

# Returns a list of all transactions.

    def get_transaction_history(self):
        """Return the transaction history"""
        return self.transaction_history
    
#Run the program.

def atm_simulation():
    atm = ATM()
    
    print("Welcome to the ATM Machine")
    time.sleep(1)

#Enter the correct PIN.

    pin = int(input("Please enter your ATM PIN: "))

    if not atm.validate_pin(pin):
        print("Invalid PIN. Exiting...")
        return


#Select an option from the menu to perform different ATM functions.

    while True:
        print("""
        Please choose an option:
        1. Balance Inquiry
        2. Cash Withdrawal
        3. Cash Deposit
        4. PIN Change
        5. Transaction History
        6. Exit
        """)

#Follow the prompts for each option.      
 
        try:
            option = int(input("Enter your choice: "))
        except ValueError:
            print("Please enter a valid option")
            continue

        if option == 1:
            print(f"Your current balance is {atm.inquire_balance()}")
        elif option == 2:
            withdraw_amount = int(input("Please enter withdraw amount: "))
            withdrawn = atm.withdraw_cash(withdraw_amount)
            if withdrawn is not None:
                print(f"{withdraw_amount} is debited from your account")
                print(f"Your updated balance is {atm.inquire_balance()}")
            else:
                print("Insufficient balance")
        elif option == 3:
            deposit_amount = int(input("Please enter deposit amount: "))
            atm.deposit_cash(deposit_amount)
            print(f"{deposit_amount} is credited to your account")
            print(f"Your updated balance is {atm.inquire_balance()}")
        elif option == 4:
            new_pin = int(input("Enter new PIN: "))
            atm.change_pin(new_pin)
            print("PIN changed successfully")
        elif option == 5:
            history = atm.get_transaction_history()
            if history:
                print("Transaction History:")
                for transaction in history:
                    print(transaction)
            else:
                print("No transactions yet.")

#Exit the program by choosing option 6

        elif option == 6:
            print("Exiting...")
            break
        else:
            print("Please enter a valid option")

if __name__ == "__main__":
    atm_simulation()