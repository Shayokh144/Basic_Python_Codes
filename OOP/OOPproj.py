
from abc import ABCMeta, abstractmethod
from random import randint
class Account(metaclass= ABCMeta):
    @abstractmethod
    def createAccount(self, name, nId, initialDeposit):
        return 0
    def authentication(self, nId ,accountNumber):
        return 0
    def withdraw(self, withdrawAmount):
        return 0
    def deposit(self, depositAmount):
        return 0
    def displayBalance(self):
        return 0



class SavingsAccount(Account):
    def __init__(self):
        #print("called")
        self.savingsAccount = {}
    def createAccount(self, name, nId, initialDeposit):
        self.accountNumber = randint(10000,99999)
        self.savingsAccount[self.accountNumber] = [name, nId, initialDeposit]
        print("acc details of acc no.{0}".format(self.accountNumber),self.savingsAccount[self.accountNumber])

    def authentication(self, nId ,accountNumber):
        if accountNumber in self.savingsAccount:
            if self.savingsAccount[accountNumber][1] == nId:
                print("hellow {0}".format(self.savingsAccount[accountNumber][0]))
                self.accountNumber = accountNumber
                return True
            else:
                print("failed!!!!")
                return False
        else:
            print("failed!!!!")
            return False
    def withdraw(self, withdrawAmount):
        if withdrawAmount <= (self.savingsAccount[self.accountNumber][2]):
            self.savingsAccount[self.accountNumber][2] -= withdrawAmount
            print("withdraw successfully")
            self.displayBalance()
        else:
            print("insufficient balance")
    def deposit(self, depositAmount):
        self.savingsAccount[self.accountNumber][2] += depositAmount
        print("operation succesful")
        self.displayBalance()

    def displayBalance(self):
        print("your account balance {0}".format(self.savingsAccount[self.accountNumber][2]))




savingsAccountObj = SavingsAccount()



while True:
    print("Enter 1 to create new acc\n 2 to access exixting acc\n 3 to exit")
    userChoice = int(input())
    if userChoice == 1:
        print("enter name")
        name = input()
        print("enter nId")
        nId = input()
        print("Enter initial deposit")
        deposit = int(input())
        savingsAccountObj.createAccount(name, nId, deposit)
    if userChoice == 2:
        print("enter nId")
        nId = input()
        print("Enter acc no")
        accountNumber = int(input())
        authStatus = savingsAccountObj.authentication(nId,accountNumber)
        if authStatus == True:
            print("Enter 1 to withdraw\n 2 to deposit\n 3 to display\n 4 to back")
            userChoice = int(input())
            if userChoice == 1:
                print("Enter Amount")
                amount = int(input())
                savingsAccountObj.withdraw(amount)
            elif userChoice == 2:
                print("Enter Amount")
                amount = int(input())
                savingsAccountObj.deposit(amount)
            elif userChoice ==3:
                savingsAccountObj.displayBalance()
            else:
                break

