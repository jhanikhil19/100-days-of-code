#F String
import math

me = "Harry"
a1=3
c="This is %s %s"%(me,a1)
print(c)

d="this is {} {}"
e=d.format(me,a1)
print(e)
d1="this is {1} {0}"
e1=d1.format(me,a1)
print(e1)
e2=f"this is {me} {a1} {math.cos(0)}"
print(e2)
