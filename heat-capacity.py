# The amount of energy required to increase the temperature of one gram of a 
# material by one degree Celsius is the material’s specific heat capacity, C. 
# The total amount of energy required to raise m grams of a material by 
# ΔT degrees Celsius can be computed using the formula:
# q = mCΔT.
# Write a program that reads the mass of some water and the temperature change
# from the user. Your program should display the total amount of energy that 
# must be added or removed to achieve the desired temperature change.
# Hint: The specific heat capacity of water is 4.186 J
# g◦C. Because water has a density of 1.0 gram per millilitre, you can use 
# grams and millilitres interchangeably in this exercise.
# Extend your program so that it also computes the cost of heating the water. 
# Electricity is normally billed using units of kilowatt hours rather 
# than Joules. In this exercise, you should assume that electricity 
# costs 8.9 cents per kilowatt-hour. Use your program to compute the cost 
# of boiling water for a cup of coffee.

def all_Data():
    masswater = float(input("What is the mass of water? "))
    tempwater = float(input("What is the temp of water? "))
    heatcapac = 4.186
    eleccosts = 8.9
    import numpy as np
    joul2kwat = 2.77 * np.exp(20**(-7))
    totalgram = masswater * heatcapac * tempwater
    totalgramk = totalgram * joul2kwat
    totalcost = totalgramk * eleccosts
    print("Energy in Joules: ", totalgram)
    print("Energy in others: ", eleccosts)
    
all_Data()

