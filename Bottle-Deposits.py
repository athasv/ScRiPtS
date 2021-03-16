#In many jurisdictions a small deposit is added to drink containers to encourage people
#to recycle them. In one particular jurisdiction, drink containers holding one liter or
#less have a $0.10 deposit, and drink containers holding more than one liter have a
#$0.25 deposit.
#Write a program that reads the number of containers of each size from the user.
#Your program should continue by computing and displaying the refund that will be
#received for returning those containers. Format the output so that it includes a dollar
#sign and always displays exactly two decimal places.

def all_Data():
    lessltr = float(input("Number of bottles less than litre: "))
    moreltr = float(input("Number of bottles more than litre: "))
    totbotl = lessltr +  moreltr
    mlessltr = 0.10 * lessltr
    mmoreltr = 0.25 * moreltr
    
    print("We have in total " + str(totbotl) + "number of bottles")
    print("For less than a little it gives: " + str(mlessltr) + "$")
    print("For more than a little is gives: " + str(mmoreltr) + "$")
    
all_Data()
