lst =[7,2,3,9,14,21]
l1=[]
l2=[]
lst.sort()
print(lst)
i = 0
while i<len(lst):
    if i%2==0:
        l1.append(lst[i])
    else:
        l2.append(lst[i])
    i+=1

print(max(sum(l1),sum(l2)),min(sum(l1),sum(l2)))