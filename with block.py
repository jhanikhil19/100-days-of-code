# f=open("nik.txt")
# f.close()

#alternate for this kind of things is as follows
#in this mode you don't need to close the file

with open("nik.txt") as f:
    a=f.read(10) #read till the pointer located --- it starts counting from 1
    print(a)
    print(type(a))

#the chunk below the with function will also open and close the file in its own manner since its outside the with.
#It will work normally.

f=open("nik.txt")
print(f.readline())
f.close()