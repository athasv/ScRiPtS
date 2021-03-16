# Develop a program that reads a four-digit integer from the user and displays
# the sum
# of the digits in the number. For example, if the user enters 3141 then your
# program should display 3+1+4+1=9


def d(n):
    sum = 0
    for i in n:
        sum = sum + int(i)
    print(sum)


d("012345678910")


def dd():
    test_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    res = []
    for ele in test_list:
        sum = 0
        for digit in str(ele):
            sum += int(digit)
        res.append(sum)
    print("List Integer Summation : " + str(res))


dd()

test_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
res = list(map(lambda ele: sum(int(sub) for sub in str(ele)), test_list))
# https://www.geeksforgeeks.org/python-program-to-find-sum-of-elements-in-list/
# https://www.sanfoundry.com/python-program-sum-elements-list-recursively/
total = 0

# creating a list
list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for ele in range(0, len(list1)):
    total = total + list1[ele]
print("Sum of all elements in given list: ", total)
