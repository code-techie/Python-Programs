def pc(n):
    for i in range(2,n):
        if n%i==0:
            print("Not Prime Number")
            break
        else:
            print("Prime Number")
            break 
pc(134)