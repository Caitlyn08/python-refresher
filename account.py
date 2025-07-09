class Account:
    def __init__(self, name, account_number, balance):
        self.name = name
        self.account_number = account_number
        self.balance = balance

    def withdraw(self, number):
        if number > self.balance or number < 0:
            raise ValueError("not valid")
        self.balance -= number
        return self.balance

    def deposit(self, number):
        if number < 0:
            raise ValueError("not valid")
        self.balance += number
        return self.balance

    def current_balance(self):
        return self.balance
