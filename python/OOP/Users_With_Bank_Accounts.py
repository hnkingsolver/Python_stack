class BankAccount:
    def __init__(self, nameOfUser, int_rate):
        self.interest = int_rate
        self.name = nameOfUser
        self.account_balance = 0

    def make_deposit(self, amount):
        self.account_balance += amount
        return self

    def make_withdrawal(self, amount):
        self.account_balance -= amount
        if self.account_balance < 0:
            self.account_balance = self.account_balance -5
            print("insuffcient funds. charging a $5 fee.")
        return self

    def display_account_balances(self):
        self.account_balance
        print(self.account_balance)
        return self

    def yield_interest(self):
        # self.balance = self.balance * self.interest + self.balance
        if self.account_balance > 1:
            total_interest = self.account_balance * self.interest
            self.account_balance += total_interest
        return self


class User:
    def __init__(self, nameOfUser, emailOfUser):
        # print("__init__ has run!")
        self.name = nameOfUser
        self.email = emailOfUser
        self.account = BankAccount(nameOfUser,0.10)
    #methods        

    def make_withdraw(self,amount):
        self.account.make_withdrawal(amount)
        return self
    
    def make_deposit(self,amount):
        self.account.make_deposit(amount)
        return self
        
    def display_account_balance(self):
        self.account.display_account_balances()
        # print("User:", self.name, "i", "balance", self.account)
        return self
        
#instances
Devin = User("Devin", "ddd@gmail.com")
Tanner = User("Tanner","ttt@gmail.com")
Hannah = User ("Hannah","hhh@gmail.com")


Devin.make_deposit(1000).make_withdraw(500).make_deposit(1000).make_withdraw(2000).display_account_balance()
Tanner.make_deposit(3000).display_account_balance()
Hannah.make_deposit(10000).display_account_balance().make_withdraw(5000).display_account_balance()
