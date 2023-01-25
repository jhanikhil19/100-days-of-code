l = 10

def function1(n):
    l=5
    print("LOCAL SCOPE:  l=",l,"and n=",n)

n=int(input("Enter value of n"))
function1(n)
print("GLOBAL SCOPE:  l=", l, "and n=", n)


def nik():
    x=20
    def akhil():
        global x
        x=88
        print("The value of x is ", x) #akhil's
    print("The value of x is ",x)#nik's
    akhil()
    print("The value of x is ", x)#nik's
nik()
print("The value of x is ", x) #global
