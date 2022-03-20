class Bank:
    def __init__(self, int_rate, balance):
        self.Palance=balance
        self.rate=int_rate
    def deposit(self, amount):
        self.Palance+=amount
        return self
    def withdraw(self, amount):
        if self.Palance>amount:
            self.Palance-=amount
        else:
            print('Insufficient funds: Charging a {}$fee" and deduct {}$',amount,amount)
        return self
    def display_account_info(self):
        print("Balance =",self.Palance)
        return self
    def yield_interest(self):
        self.Palance=self.Palance+self.Palance*self.rate
        return self
class User:
    def  __init__ (self,name , email , BankAccount):
        self.name =name
        self.email = email
        self.Bank = BankAccount
    def make_deposit(self, amount):
        self.Bank.deposit(amount)
    def display_user_balance(self):
        print(self.Bank.display_account_info())
    def make_withdrawal(self,amount):
        self.Bank.withdraw(amount)
    def transfer_money(self,self2,amont):
        self.Bank.withdraw(amont)
        self2.Bank.deposit(amont)
israaAccount= Bank(0.5,100)
israa = User('israa','israa@hotmail.com',israaAccount)
israa.make_deposit(20)
israa.display_user_balance()
israa.make_withdrawal(30)
israa.display_user_balance()

