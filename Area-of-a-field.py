#Create a program that reads the length and width of a farmer’s field from the user in
#feet. Display the area of the field in acres.
#Hint: There are 43,560 square feet in an acre.

def all_Data():
    inData1 = float(input("How much is the width? "))
    inData2 = float(input("How much is the length? "))
    permVal = 43.560
    totResf = inData1 + inData2
    totResa = (inData1 + inData2) / permVal
    print("The result in feet is: ", totResf)
    print("The result in feet is: ", totResa)

all_Data()
