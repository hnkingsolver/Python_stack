class User:
    def __init__(self, nameOfUser, balanceOfUser):
        # print("__init__ has run!")
        self.name = nameOfUser
        self.balance = balanceOfUser
    #methods        

    def make_withdraw(self,amount):
        # if self.balance >= amount:
        self.balance -= amount
        print(self.balance)
        return self
    
    def make_deposit(self,amount):
        # if self.balance >= amount:
        self.balance += amount
        print(self.balance)
        return self   
        
    def display_account_balance(self):
        print(self.balance)
        return self   
        
#instances
Devin = User("Devin", 1000)
Tanner = User("Tanner",900)
Hannah = User ("Hannah",800)

# Devin.make_withdraw(50)
# Devin.make_makedeposit(100)
# Devin.make_makedeposit(50)
# Devin.make_makedeposit(900)
# Devin.display_account_balance()

# Tanner.make_makedeposit(1000)
# Tanner.make_makedeposit(1100)
# Tanner.make_withdraw(300)
# Tanner.make_withdraw(700)
# Tanner.display_account_balance()

# Hannah.make_makedeposit(2000)
# Hannah.make_withdraw(100)
# Hannah.make_withdraw(300)
# Hannah.make_withdraw(400)
# Hannah.display_account_balance()


#CHAINING METHOD // MAKES THIS EASIER/BETTER TO READ
# Devin.make_withdraw(50).make_makedeposit(100).make_makedeposit(50).make_makedeposit(900).display_account_balance()
# Tanner.make_makedeposit(1000).make_makedeposit(1100).make_withdraw(300).make_withdraw(700).display_account_balance()
# Hannah.make_makedeposit(2000).make_withdraw(100).make_withdraw(300).make_withdraw(400).display_account_balance()
