from cryptography.fernet import Fernet
import random


class Bank():
    #def __init__(self):
    #    self.name = name
    #    self.passowrd = password

    def openAccount(self):
        name = input("Name: ")
        #surname = input("Surname: ")
        #email = input("e-mail: ")
        password = input("password: ")
        acountNumber = random.randint(100000,999999)
        print("Account Number given: " +str(acountNumber))
        return(name, password, acountNumber)

    def getIntoAccount(self):
        promptAcount = input("Acount Number: ")
        print(acountNumber)
        promptPassword = input("Password: ")
        if promptAcount == acountNumber:
            print("got one")
            if promptPassword == passowrd:
                print("you in")

    def deleteAccount(self):
        print("New account balance: " +str(self.balance))


bank = Bank()

name, password, acountNumber = bank.openAccount()
bank.getIntoAccount()
