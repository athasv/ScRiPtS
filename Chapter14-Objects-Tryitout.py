#Exercise 2
class BankAccount:
    def __init__(self, name, accNum):
        self.name=name
        self.accNum=accNum
        self.balance=0.0
    
#    def __str__(self):
#        msg = str(self.name) + "your account is: " + str(self.accNum) + " and your balance is: " + str(self.balance) + " with withdrawn: " + str(self.withdrawn)
#        return msg
    
    def displayBalance(self):
        print("Your balance is: " + str(self.balance))
        
    def makeDeposit(self, amountofDeposit):
        amountofDepositUpdated = 0.0
        amountofDepositUpdated = amountofDeposit + self.balance
        if self.balance == 0.0:
            previous = self.balance
        if self.balance != 0.0:
            previous = amountofDepositUpdated + self.balance
        total = []
        total.append(amountofDepositUpdated)
        print("Your deposit is: " + str(amountofDeposit))
        print("Your previous total was: " + str(previous))
        print("Your new total  is: " + str(amountofDepositUpdated))

instanceClient = BankAccount("Jorge", 100)

instanceClient.makeDeposit(100)
instanceClient.makeDeposit(200)