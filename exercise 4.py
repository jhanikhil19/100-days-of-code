# Pattern Printing
# input = n
# Boolean = True or False
# true
# *
# **
# ***
# ****
# false
# ****
# ***
# **
# *
# print(bool(1))#True
# print(bool(0))#False

n=(int(input("Enter the number of lines you want in the pattern of *")))
order2=int(input("Enter True for increasing order and False for decreasing order of pattern of *"))
order1=bool(order2)
# print("Order1",order1)
# print("Order2",order1)
if (order1==True):
    #using foor loop
    for i in range (1,n+1):
        #for j in range (0,i):
            print("*"*i)
    #using while loop
    i=0
    while(i<n+1):
        print("*"*i)
        i=i+1
elif (order1==False):
    #using for loop
    for i in range (1,n+1):
        for j in range (1,n+2-i):
            print("*",end="")
        print()
    #using while loop
    i=n
    while(i>=0):
        print("*"*i)
        i=i-1

else:
    print("Invalid input")
