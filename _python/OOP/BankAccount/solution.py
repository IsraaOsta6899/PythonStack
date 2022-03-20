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
account1=Bank(0.5,100)
account2=Bank(0.5,200)
account1.deposit(10).deposit(20).deposit(20).withdraw(50).yield_interest().display_account_info()
account2.deposit(10).deposit(20).withdraw(50).withdraw(50).withdraw(50).withdraw(50).yield_interest().display_account_info()
