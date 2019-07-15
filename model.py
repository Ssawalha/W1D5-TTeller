import json
import os
from random import randint

DIR = os.path.dirname(__file__)
DATAFILENAME = "accounts.json"
DATAPATH = os.path.join(DIR, DATAFILENAME)

class AuthenticationError(Exception):
    pass

class Account:
    data_path = DATAPATH

    def __init__(self, account_num=""):
        # populate self.attributes for a bank account
        self.account_num = account_num
        self.pin = None
        self.balance = 0.0
        self.data = {}
        self.first = ''
        self.last = ''
        self.load()

    def load(self):
        try:
            with open(self.data_path) as json_file:
                self.data = json.load(json_file)
        
        except FileNotFoundError:
            pass
        #print("loaded data:",self.data)
        if self.account_num in self.data:
            self.balance = self.data[self.account_num]["balance"]
            self.pin = self.data[self.account_num]["pin"]
            self.first = self.data[self.account_num]["first"]
            self.last = self.data[self.account_num]["last"]

    def create_account(self, pin, first, last):
        self.pin = pin
        self.first = first
        self.last = last
        self.balance = 0
        account_num = randint(100000,999999)
        check_account_num = False
        while check_account_num == False:
            if account_num in self.data:
                account_num = randint(100000,999999)
            else:
                check_account_num = True
        self.account_num = str(account_num)
        self.data[account_num] = {'pin':self.pin,'balance':self.balance,'first':self.first,'last':self.last}
        self.save()

    def save(self):
        with open(self.data_path, 'w') as json_file:
            json.dump(self.data, json_file)

    def deposit(self, amount):
        currentbal = self.balance
        newbal = currentbal + amount
        self.data[self.account_num]['balance'] = newbal
        self.save()
        self.load()

    def withdraw(self, amount):
        if amount > self.balance:
            return False
        else:
            self.data[self.account_num]['balance'] = (self.balance - amount)
            self.save()
            self.load()

    def show_balance(self):
        return self.balance
    
    @classmethod
    def login(cls, account_num, pin):
        account = cls(str(account_num))
        if str(pin) != account.pin:
            return None
        return account


# if __name__ == "__main__":
#     account_num = "123456"
#     pin = "1234"
#     account = Account(account_num)
#     #print(account.pin)
#     print(account.login(account_num,pin))
#     print(account.account_num)
#     print(account.balance)
#     account.deposit(2)
#     print(account.balance)
#     account.withdraw(2)
#     print(account.balance)

