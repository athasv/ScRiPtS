#The program that you create for this exercise will begin by reading the cost 
#of a meal ordered at a restaurant from the user. Then your program will 
#compute the tax and tip for the meal. Use your local tax rate when computing 
#the amount of tax owing. Compute the tip as 18 percent of the meal amount 
#(without the tax). The output from your program should include the tax amount,
#the tip amount, and the grand total for the meal including both the tax and 
#the tip. Format the output so that all of the values are displayed using two 
#decimal places.

#def all_Data():
#    mealCost = float(input("How much is the meal? "))
#    localtax = 0.45
#    localtip = 0.03
#    totalmon = (mealCost * localtax) + (mealCost * localtip) + mealCost
#    print("The total amount to pay is: " + str(totalmon))
#all_Data()

def all_Data(total, tax, tip):
    totalmon = (total * tax) + (total * tip) + total
    print("The total amount to pay is: " + str(totalmon))
    
all_Data(20.0,0.45,0.03)