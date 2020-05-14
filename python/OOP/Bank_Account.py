class BankAccount:
    def __init__(self, int_rate, balances):
        self.interest = int_rate
        self.balance = balances

    def make_deposit(self, amount):
        self.balance += amount
        print(self.balance)
        return self

    def make_withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            print(self.balance)
            return self
        else:
            self.balance -= 5
            print(self.balance)
            print("Insuffcient funds. Charging a $5 fee.")
            return self

    def display_account_balance(self):
        print(self.balance)
        return self

    def yield_interest(self):
        # self.balance = self.balance * self.interest + self.balance
        self.balance *= self.interest + 1
        print(self.balance)
        return self

Account_1 = BankAccount(.02, 5000)
Account_2 = BankAccount(.04, 10000)


# Account_1.make_withdraw(7000).make_deposit(1000).make_deposit(1000).make_deposit(5).yield_interest().display_account_balance()
# Account_2.make_deposit(200).make_deposit(1000).make_withdraw(3000).make_withdraw(300).make_withdraw(5000).make_withdraw(3000).display_account_balance()