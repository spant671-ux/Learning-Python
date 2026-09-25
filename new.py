class BankAccount:
    def __init__(self, balance):
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def get_balance(self):
        return self.balance


account = BankAccount(5000)
account.deposit(1000)
print(account.get_balance())
