class User:
    def  __init__ (self,name , email , account):
        self.name =name
        self.email = email
        self.account_balance = account
    def make_deposit(self, amount):
        self.account_balance += amount	
        return self
    def display_user_balance(self):
        print(self.account_balance)
        return self
    def make_withdrawal(self,amount):
        self.account_balance -=amount
        return self
    def transfer_money(self,self2,amont):
        self.make_withdrawal(amont)
        self2.make_deposit(amont)
        return self


israa=User("israa", 'israa-osta@hotmail.com',100)
alaa=User("alaa", 'alaa-osta@hotmail.com',200)
aya=User("aya", 'aya-osta@hotmail.com',300)
israa.make_deposit(20).make_deposit(10).make_deposit(30).make_withdrawal(40)
israa.display_user_balance()

alaa.make_deposit(20).make_deposit(10).make_withdrawal(40).make_withdrawal(60).display_user_balance()


aya.make_deposit(20).make_withdrawal(50).make_withdrawal(40).make_withdrawal(60).display_user_balance()


israa.transfer_money(aya,20).display_user_balance()

aya.display_user_balance()


