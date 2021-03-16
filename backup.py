# Exercise 2
class BankAccount:

    def __init__(self, name, accNum):

        self.name = name
        self.accNum = accNum
        self.balance = 0.0

    def displayBalance(self):

        print("Your balance is: " + str(self.balance))

    def makeDeposit(self, amountofDeposit):
        self.balance = self.balance + amountofDeposit
        print("Your deposit is: " + str(amountofDeposit))
        print("Your total is: " + str(self.balance))

    def withdraw(self, amounttoWithdraw):
        if self.balance >= amounttoWithdraw:
            self.balance = self.balance - amounttoWithdraw
            print("Your withdrew: " + str(amounttoWithdraw))
            print("Your total is: " + str(self.balance))
        if self.balance < amounttoWithdraw:
            print("Your withdrew: " + str(amounttoWithdraw))
            print("Your withdrew denied, not enough funds")


instanceClient = BankAccount("Jorge", 100)

instanceClient.makeDeposit(1000.0)
instanceClient.withdraw(100.0)
instanceClient.withdraw(100.0)
instanceClient.withdraw(100.0)
instanceClient.withdraw(100.0)
instanceClient.makeDeposit(1000.0)
instanceClient.makeDeposit(1000.0)
instanceClient.makeDeposit(1000.0)
instanceClient.makeDeposit(1000.0)
