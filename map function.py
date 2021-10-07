def add(n):
    return n+n
num = (1,2,3,4,5)
result = map(add, num)
print(list(result))