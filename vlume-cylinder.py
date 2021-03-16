# The volume of a cylinder can be computed by multiplying the area of its circular
# base by its height. Write a program that reads the radius of the cylinder, along with
# its height, from the user and computes its volume. Display the result rounded to one
# decimal place.
import numpy as np

def all_Data():
    area = int(input("What is the area? "))
    heig = int(input("What is the heig? "))
    radi = int(input("What is the radi? "))
    volu = area * heig * radi * np.pi
    surf = ((2*np.pi*radi) * heig) + ((np.pi*radi**2)*2)
    print("The total volume  1is: ", volu)
    print("The total surface is: ", surf)
all_Data()






