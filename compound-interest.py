# Pretend that you have just opened a new savings account that earns 4 percent 
# interest per year. The interest that you earn is paid at the end of the year, 
# and is added to the balance of the savings account. Write a program that 
# begins by reading the amount of money deposited into the account from the 
# user. Then your program should compute and display the amount in the savings 
# account after 1, 2, and 3 years. Display each amount so that it is rounded 
# to 2 decimal places.

def all_Data():
    interest = 0.04
    deposit = float(input("How much money inside the account? "))
    one = deposit * interest + deposit
    two = one * interest + one
    three = one * interest + two
    print("The amount of the first year is: ",  one)
    print("The amount of the first year is: ",  two)
    print("The amount of the first year is: ",  three)
    
all_Data()

