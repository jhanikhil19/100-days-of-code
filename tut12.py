#elseif

var1 = 88
var2 = 23
print("Enter input")
var3=int(input())
if var3<=var1:
    if var3 >= var2:
        print(var3,"is in the range between",var1,"and",var2)
    else:
        print(var3,"is smaller than both",var1,"and",var2)
else:
    print(var3,"is bigger than both",var1,"and",var2)


if var3>=var1:
    print(var3,"is largest")
elif var3<=var1 and var3>=var2:
    print(var3,"in the limits of ",var1,"and",var2)
else:
    print(var3,"is smaller than",var1,"and",var2)

list1=[1,3,5,1,4,44,52]
print(5 in list1)
if 5 in list1:
    print("yES its in list")
