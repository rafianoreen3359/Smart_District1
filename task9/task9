""" Task: 

● Banking System: Build a `BankAccount` class that stores an owner name and balance 
securely. The balance must be inaccessible from outside the class. Deposits and 
withdrawals go through validated methods only. Print any account and get a clean, 
readable summary."""

class BankAccount:

    def __init__(self, owner, balance):
        self.owner = owner
        self.__balance = balance 

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print("Deposit successful!")
        else:
            print("Amount must be greater than zero.")

    def withdraw(self, amount):
        if amount <= 0:
            print("Amount must be greater than zero.")
        elif amount > self.__balance:
            print("Insufficient balance!")
        else:
            self.__balance -= amount
            print("Withdrawal successful!")

    def __str__(self):
        return f"Owner: {self.owner}\nBalance: Rs. {self.__balance:.2f}"

account1 = BankAccount("Ali", 5000)

account1.deposit(2000)

account1.withdraw(1000)

print("\n--- Account Summary ---")
print(account1)
