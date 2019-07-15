import model as m
from random import randint

def mainmenu():
    print("Welcome to Terminal Teller! \n")
    print('1) Create account')
    print('2) Log in')
    print('3) Quit')
    selection = int(input('Your choice: '))
    return selection

def create_account():
    print("Account creation\n")
    first = input('First name: ')
    last = input('Last name: ')
    pin = input('4-digit PIN: ')
    while len(pin)!=4:
        print('Please retype 4-digit PIN:')
        pin = input('4-digit PIN: ')
    confirm_pin = input('Confirm PIN: ')
    while confirm_pin != pin:
        pin = input('PIN mismatch, please retype PIN')
        confirm_pin = input('Confirm PIN: ')   
    if confirm_pin == pin:
        return pin, first, last

def create_acc_success(account_num):
        print('\nYour account has been created, your account number is: {}.'.format(account_num))

def login():
    account_num = str(input("Account number: "))
    pin = input("PIN: ")
    return account_num, pin

def account_options(account):
    print('Hello, {f} {l} ({n})\n'.format(f = account.first, l = account.last, n = account.account_num))
    print('1) Check balance')
    print('2) Withdraw funds')
    print('3) Deposit funds')
    print('4) Sign out')
    selection2 = int(input('\nYour Choice:'))
    return selection2

def show_balance(balance):
    print('\nYour balance is: $', balance)

def withdraw_funds():
    amount = int(input('How much to withdraw? $'))
    return amount

def withdraw_message(amount):
        print('Withdrawing amount ${}'.format(amount))

def insufficient_funds(fundbool):
    if fundbool == False:
        print('! ! INSUFFICIENT FUNDS ! !')

def deposit_funds():
    amount = int(input('How much to deposit? $'))
    return amount

# if __name__ == "__main__":
#         accountnum = 123456
#         accountnum = str(accountnum)
#         pin = 1234
#         account = m.Account(accountnum)
#         #print(account.balance)
#         account_details = m.Account.login(accountnum, pin)
#         print(account_details.balance)