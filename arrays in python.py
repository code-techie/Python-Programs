import array as arr

# double('d') for decimel numbers and 'i' for integers

abc = arr.array('d', [2.5, 4.9, 6.7])

abc[0]=9.4   
                              # assigning new value to abc[0]
abc.insert(1, 3.5)            # inserting value '3.5' at index '1'

print(f'this is required value:\n{abc}')

abc.reverse()                # reversing the array

for x in abc:                # Traversing the array
    print(x)
# array concatenation
d = arr.array('d',[1.4,5.2,9.7])
e =arr.array('d')
e = abc+d
print(e)
# find index of element

print(e.index(5.2))

# removing the element
e.remove(1.4)
print(e)
# removing using index
e.pop(5)
print(e)
# removing using index
del e[2]
print(e)
# counting the occurence of number
print(e.count(4.9))

# Finding the lenth of array

print(len(e))
