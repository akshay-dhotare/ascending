import datetime

class account:
    def __init__(self):
     self.deposit=5000

    def inc_deposit(self):
        self.deposit+=1
        self.display_deposit()

    def dec_deposit(self):
        self.deposit-=1
        self.display_deposit()

    def display_deposit(self):
        date=datetime.datetime.now()
        print(f"total deposit at {date} is = {self.deposit}")

d1=account()
d1.inc_deposit()
d1.dec_deposit()
d1.display_deposit()
