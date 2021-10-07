import re
# 'Match' function

wik ='Is this RegEx'
w = re.match('is',wik,re.I)      # 'Match' function checks only at begining of the string
if w:
    print('match found:',w.group())
else:
    print("not match")


wi ='Is this RegEx'
w = re.match('.*is.*ex$',wi,re.I)      # This function checks all the lines of the string only
if w:
    print('match found:',w.group())
else:
    print("not match")


# 'Search' function
v = 'is this regular expression'
x = re.search('this', v,re.I)        # 'search' function checks throghout the string
if x:
    print('Match found:',x.group())
else:
    print('Match not found')

# substitute (sub) function
line = 'this is a python session-topic RegEx'

# delete text after the 'session'

ad = re.sub(r'-.*$' ,"", line)
print("Updated line is:",ad)
# print only digits in the string
num= 'bhushan:77542'

num = re.sub(r'\D',"", num)
print('new num is:',num)

# findall function
# (find the all the occurences of pattern and gives the list)
a = re.findall('is', line)
print(a)

# split function
l = re.split('\s', line)           # splitting string at blank spaces
# '\s' = used for blank space
print(l)

k = re.split('\s', line,2)
# string split two time only at white spaces
print(k)
g = re.split('this', line)
print(g)