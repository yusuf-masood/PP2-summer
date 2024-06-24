class BankAccount:
    def __init__(self, owner='', balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited: {amount}")
        print(f"New Balance: {self.balance}")

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            print(f"Withdrew: {amount}")
            print(f"Remaining Balance: {self.balance}")
        else:
            print("Insufficient balance for withdrawal.")

# Create an instance of BankAccount
myAccount = BankAccount('Orynbay Aruzha', balance=15000)

# Test deposit and withdraw methods
myAccount.deposit(2000)    # Testing deposit
myAccount.withdraw(1000)   # Testing withdrawal within balance
myAccount.withdraw(20000)  # Testing withdrawal exceeding balance
