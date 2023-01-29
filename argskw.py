def function_name_print(a,b,c,d):
    print(a,b,c,d)

function_name_print("ABC","BCD","CDE","DEF")

#in args the tuple is passed.


def function_args(*args):
    print(type(args))
    print(args[0])

nam=["ABC","BCD","CDE","DEF"]
function_args(*nam)
print(type(nam))



def function_args(normal, *args, **kwargs):
    print(normal)
    for item in args:
        print(item)
    print("\n\n")
    for key,value in kwargs.items():
        print(f"{key} is right now residing at {value}.")

nam=["ABC","BCD","CDE","DEF"]
kw={"Nik":"GERMANY","DS":"CANADA","SS":"USA"}
normal="THIS IS A BASIC LINE"
function_args(normal,*nam,**kw)
# print(type(nam))
