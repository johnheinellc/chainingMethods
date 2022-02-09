class User:
#
    bank_name = "First National Dojo"
#
    def __init__(self , name, account_balance):
        self.name = name
        self.account_balance = account_balance

##function
    def display_user_balance(self):
        print(f"Welcome {self.name} your balance is: {self.account_balance}")

##withdraw
    def make_withdrawal(self, amount):
        self.account_balance -= amount
        return self
##deposit
    def make_deposit(self, amount):
        self.account_balance += amount
        return self
##transfer
    def transfer_money(self, other_user, amount):
        self.make_withdrawal (amount)
        other_user.make_deposit (amount)
        return self



## user info
User1 = User("Guido van Rossum", 4000)
User2 = User("Monty Python", 2500)
User3 = User("John Heine",1000)
## print transfer
User1.transfer_money(User3,100)
# print(User1)
User1.make_deposit(100).make_deposit(15).make_deposit(35).make_withdrawal(150).display_user_balance()
# print(User2)
User2.make_withdrawal(2500).make_deposit(500).make_withdrawal(250).make_deposit(5).display_user_balance()
# print(User3)
User3.make_withdrawal(900).make_deposit(1000).make_withdrawal(500).make_withdrawal(599).display_user_balance()
