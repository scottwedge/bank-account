from cryptography.fernet import Fernet
import random







with open('accounts.csv', mode='r', newline = '') as accounts_file:
    lines = accounts_file.readlines()

    for line in lines:
        new_line = line.split(',')
        print(new_line[1,1])




#message = "my deep dark secret".encode()
#key = Fernet.generate_key() # Store this key or get if you already have it
#f = Fernet(key)
#encrypted = f.encrypt(message)
#decrypted = f.decrypt(encrypted)
#if message == decrypted:
#    print("OOOOOP")


'''

class Bank():
    #def __init__(self):
    #    self.name = name
    #    self.passowrd = password

    def openAccount(self):
        name = input("Name: ")
        #surname = input("Surname: ")
        #email = input("e-mail: ")
        password = input("password: ")
        accountNumber = random.randint(100000,999999)
        print("Account Number given: " +str(accountNumber))
        return(name, password, accountNumber)

    def getIntoAccount(self):
        promptAccount = input("Account Number: ")
        print(accountNumber)
        promptPassword = input("Password: ")
        if promptAccount == accountNumber:
            print("got one")
            if promptPassword == password:
                print("you in")

    def deleteAccount(self):
        print("New account balance: " +str(self.balance))


bank = Bank()

name, password, accountNumber = bank.openAccount()
bank.getIntoAccount()
'''
