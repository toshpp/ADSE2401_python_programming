# python script to demonstrate the use instance, static and class method
# real world scenario

# Import the regular expressions method
import re

class BankAccount:
    # Class attribute (shared across all instances)
    interest_rate = 0.05  # 5% annual interest rate

    # constructor
    def __init__(self, account_holder, balance=0):
        self.account_holder = account_holder
        self.balance = balance

    # -------------------------------------
    # Instance method(s)
    # -------------------------------------

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            # Display the new balance
            print(f"[{self.account_holder}] deposited KES {amount:.2f}"
                  f"\nNew balance is: KES {self.balance:.2f}")
        else:
            print("Kindly note that the deposited amount must be positive.")

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            print(f"[{self.account_holder}] withdrew KES {amount:.2f}"
                  f"\nNew balance is: KES {self.balance:.2f}")
        else:
            print("Invalid withdrawal amount or insufficient funds.")

    # -------------------------------------
    # class method(s)
    # -------------------------------------
    @classmethod
    def set_interest_rate(cls, new_rate):
        if 0 <= new_rate <= 0.2:
            cls.interest_rate = new_rate
            print(f"The annual interest rate has been set to {new_rate * 100:.2f}% for all accounts!")
        else:
            print("The annual interest rate must be between 0% and 20%!")

    # -------------------------------------
    # Static method(s)
    # -------------------------------------
    @staticmethod
    def validate_account_number(account_number):
        pattern = r"^ACC\d{6}$"
        return bool(re.match(pattern, account_number))


# -------------------------------------
# Demonstration
# -------------------------------------

# create 2 bank account objects
abigail_acc = BankAccount(account_holder="ABIGAIL", balance=55000.00)
brian_acc = BankAccount(account_holder="BRIAN", balance=55000.00)

# Deposit and withdraw money
abigail_acc.deposit(1500)
brian_acc.withdraw(700)

# update the annual interest rate (class method)
BankAccount.set_interest_rate(0.08)

# validate new account numbers (static method)
print("\nValidating new account numbers...\nPlease wait")
print("ACC123754 is valid?", BankAccount.validate_account_number("ACC123754"))
print("Account123457 is valid?", BankAccount.validate_account_number("Account123457"))
