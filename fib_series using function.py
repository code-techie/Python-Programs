def fib(n):
    if n<0:                               # setting conditions for fib  recursion function very important
        print("incorrect output")
    elif n==1:                               # setting conditions for fib  recursion function very important                     
        return 0
    elif n==2:                               # setting conditions for fib  recursion function very important
        return 1
    else:
        return fib(n-1)+fib(n-2)
print(fib(20))