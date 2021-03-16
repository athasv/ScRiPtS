# An online retailer sells two products: widgets and gizmos. Each widget weighs 
# 75 grams. Each gizmo weighs 112 grams. Write a program that reads the number 
# of widgets and the number of gizmos in an order from the user. Then your 
# program should compute and display the total weight of the order.

def all_Data():
    w = int(input("How much widgets? "))
    g = int(input("How much gizmos? "))
    gizmos = g * 75
    widget = w * 112
    totwg = gizmos = widget
    print(totwg)
    
all_Data()

