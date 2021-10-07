import re
print(re.match('ca*t', 'caatica'))
line = "welcome to python session"
c = re.compile(".*to")              # converting to object     
res = re.findall(c, line)           # starting with anything, ending with 'to'
print(res)


d = re.compile(".*t.o")
rs = re.findall(d, line)        # there is one character after 't' and then 'o' is written
print(rs)

e = re.compile(".*t..o")      # 't' followed by any two character and then 'o'
rt = re.findall(e, line)
print(rt)                   # gives empty list means no such pattern is present in given string


yt = re.compile(".*n$")   # $ is used to find sting ends with given character or not
sr = yt.match(line)        # gives string ends with "o"
print(sr)    



