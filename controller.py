#when you are using import statements you should have a shebang line MINE ISNT WORKING FOR SOME REASON
import model as m #as renames
import view as v #as renames
import json 

def start():
    selection = 0
    while selection != 3:
        selection = v.mainmenu()
        if selection == 1: # Create account
            pin, first, last  = v.create_account()
            newaccount = m.Account()
            newaccount.create_account(pin, first, last)
            v.create_acc_success(newaccount.account_num)
            start()

        if selection == 2: #Log in
            account_num, pin = v.login()
            account_num = str(account_num)
            account = m.Account(account_num)
            account_details = account.login(account_num, pin)
            if account != None:
                option = 0
                while option != 4:  
                    option = v.account_options(account_details)
                    if option == 1: # Show Balance
                        v.show_balance(account.balance)

                    elif option == 2:# Withdraw Funds
                        amount = v.withdraw_funds()
                        if account.withdraw(amount) == False:
                            v.insufficient_funds
                        else:
                            v.withdraw_message(amount)
                            v.show_balance(account.balance)

                    elif option == 3:# Deposit Funds
                        amount = v.deposit_funds()
                        account.deposit(amount)
                        v.show_balance(account.balance)
                start() # Back to create/login menu

if __name__ == '__main__':
    start()
