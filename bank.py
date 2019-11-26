import random
import csv
from cryptography.fernet import Fernet
##PY3

#name = input("Name: ")
#password = input("password: ")
#def Create():
#    email = input("e-mail: ")
#    password = input("password: ")
#    return(email, passowrd)



class Account():
    def __init__(self, balance, overdraft, type, login, email = None, password = None):
        self.balance = balance
        self.overdraft = False
        self.type = False
        self.email = email
        self.password = password
        self.accountNumber = random.randint(100000,999999)
        self.login = False

    def openAccount(self):
        self.email = input("Email: ")
        self.password = input("Password: ")

    def isLogin(self):
        print("LOGIN TO YOUR ACCOUNT")
        promptEmail = input("Email: ")
        promptPassword = input("Password: ")
        if promptEmail == self.email:
            if promptPassword == self.password:
                print("YOUIN")
                self.login = True

    #def isOverdraft(self, bool):
    #    self.type = bool

    def displayBalance(self):
        if self.login == True:
            print("Account balance: " +str(self.balance))
        else:
            self.isLogin()

    def displayNewBalance(self):
        print("New account balance: " +str(self.balance))


    def deposit(self, amount):
        if self.login == True:
            #print(amount)
            self.balance += amount
            self.displayNewBalance()
            if self.overdraft == True:
                if self.balance >= 0:
                    self.overdraft = False
        else:
            self.isLogin()


    def withdraw(self, amount):
        print(amount)
        #self.balance -= amount
        #self.displayNewBalance()

        if self.balance < amount:
            print("Warning")
            if self.type == True:
                self.balance -= amount
                self.displayNewBalance()
                self.overdraft = True
            else:
                print("Not an overdraft account")
        else:
            self.balance -= amount
            self.displayBalance()


    def overdraftAction(self):
        if self.type == True:
            print("")
        else:
            print("No")
        return


#Write the name row of the csv file
with open('accounts.csv', mode='w', newline = '') as accounts_file:
    writer = csv.writer(accounts_file)
    writer.writerow(['Email', 'Password', 'Balance'])

while True:
    #append to the csv file as you add accounts
    account = Account(0, False, False, False, 'email', 'password')
    account.openAccount()
    with open('accounts.csv', mode='a', newline = '') as accounts_file:
        writer = csv.writer(accounts_file)#,  delimiter=' ', quotechar='|', quoting=csv.QUOTE_MINIMAL)
        writer.writerow([account.email, account.password, account.balance])

def main():
    #Create()
    #account = Account(0, False, False, False, 'email', 'password')
    #print(account.balance)
    account.openAccount()
    account.isLogin()
    #normAccound = Account(200, False, False)
    #normAccound.isOverdraft(True)
    account.displayBalance()
    #normAccound.withdraw(400)
    #normAccound.displayBalance()
    account.deposit(400)
    #normAccound.displayBalance()

main()
