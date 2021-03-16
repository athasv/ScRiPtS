# Create a program that reads two integers, a and b, from the user. 
# Your program should compute and display:
# • The sum of a and b
# • The difference when b is subtracted from a
# • The product of a and b
# • The quotient when a is divided by b
# • The remainder when a is divided by b
# • The result of log10 a
# • The result of ab
# Hint: You will probably find the log10 function in the math module helpful
# for computing the second last item in the list.

def all_data():
    a = int(input("Give a number as a: "))
    b = int(input("Give a number as b: "))
    sur = a + b
    dif = a - b
    pro = a * b
    dev = a / b
    rem = a % b
    from math import log10
    log = log10(a)
    log2 = log**b
    print(sur)
    print(dif)
    print(pro)
    print(dev)
    print(rem)
all_data()








