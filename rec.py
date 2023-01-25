# n! = n * n-1 * n-2 * ..... * 1
# n! = n * (n-1)!


def factorial_iterative(n):
    """
    :param: n Integer
    :return: n * n-1 * n-2 * ..... * 1
    """
    fac=1
    for i in range(n):
        fac=fac*(i+1)
    return fac

def factorial_rec(n):
    if (n==1):
        print(n)
        return 1
    else:
        print(n)
        return n * factorial_rec(n-1)

# 5*factorial_rec(4)
# 5*4*factorial_rec(3)
# 5*4*3*factorial_rec(2)
# 5*4*3*2*factorial_rec(1)
# 5*4*3*2*1

number=int(input("Enter number to get factorial"))
print("Factorial using iterative method",factorial_iterative(number))
print("Factorial using recursive method",factorial_rec(number))

def fibonacci(n):
    if (n==0):
        return 0
    elif (n==1):
        return 1
    else:
        return fibonacci(n-1)+fibonacci(n-2)

num=int(input("Enter number of fibonacci series you want"))
print("Fibonacci series till ",num,"is",fibonacci(num))
