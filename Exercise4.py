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

n=print(int(input("Enter the number of lines you want in the pattern of *")))
order1=print(input("Enter True for increasing order and False for decreasing order of pattern of *"))
print(order1)
if order1=="True":
    i=1
    while(i<=n):
        print("*"*i)
        i+=i
elif order1=="False":
    i=n
    while(i!=0):
        print("*"*i)
        i-=i
else:
    print("Invalid input")


