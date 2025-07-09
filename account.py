class Account:
    def __init__(self, name, account_number, balance=0):
        self.name = name
        self.account_number = account_number
        self.balance = balance

    def withdraw(self, number):
        self.balance -= number
        if number > self.balance:
            raise ValueError("Not enough balance")
        return self.balance

    def deposit(self, number):
        self.balance += number
        return self.balance

    def current_balance(self):
        return self.balance
