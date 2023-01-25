def getdate():
    import datetime
    return datetime.datetime.now()

a=str(getdate())
b = input("Enter something")
# c=a+b
# print(c)
with open("nik.txt","a+") as f:
    # a=str(getdate())
    # b = input("Enter something")
    f.write("\n"+a+"\t"+b)
    #f.write(b)
    a1=f.read()
    print(a1)
#
# xx = str(getdate())
# print(xx)
# print(type(xx))
# print(getdate())
# print(type(getdate()))