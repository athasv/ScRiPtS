# It is commonly said that one human year is equivalent to 7 dog years.
# this simple conversion fails to recognize that dogs reach adulthood in
# approximately two years. As a result, some people believe that it is better
# to count each of the first two human years as 10.5 dog years, and then count
# each additional human year as 4 dog years. Write a program that implements
# the conversion from human years to dog years described in the previous
# paragraph. Ensure that your program works correctly for conversions of less
# than two human years and for conversions of two or more human years.
# Your program should display an appropriate error message if the user enters
# a negative number.


def d(i):
    k = 10.5
    kk = k + k
    if i == 1:
        print(k)
    if i <= 2:
        print(kk)
    if i > 2:
        tot = (i - 2) * 4 + kk
        print(tot)

d(1)
d(2)
d(3)
d(100)
print("===============")
def o(v):
    kk = 21.0
    j = 99 - kk
    if v > 99:
        print("A lot")
    if v <= 99:
        if v % 2 == 1:
            print(v % j)
        if v % 2 == 0:
            print(v / j)

o(100)
o(99)
o(98)

