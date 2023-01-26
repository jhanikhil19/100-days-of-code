#lambda function is just for the conviences
#Lambda or anonymous functions

#both are equal

def minus(a,b):
    c=a-b
    return c

print(minus(10,8))

#OR

c= lambda a,b: a-b
print(c(10,8))

def n_first(n):
    return n[0]



n=[[1,4],[6,2],[3,7]]
n.sort(key=n_first)
print(n)

n=[[1,4],[6,2],[3,7]]
n.sort(key=lambda x:x[1])
print(n)

