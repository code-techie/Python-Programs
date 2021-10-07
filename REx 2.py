import re 
line = 'Thes es a python session'
x = re.findall('.es+',line)     # es occurencences one or more times
print(x)


sst = '''Here is a session 
on python session
how do you do?n'''

c = re.findall('^h.*',sst,re.M|re.I)         # '^' search only for single line, 're.I' is used to ignore case sensitivity
                                             # 're.M' is used to consider three separate lines when '^' is used
print(c)
y = re.findall('\Ah.*',sst,re.M|re.I)       # '\A' consider multiple lines to single line(line starting with 'h') 
print(y)


t = re.findall('.*n\Z',sst,re.M|re.I)       # consider multiple line to one line only(line ending with 'n')
print(t)
e = re.findall('.*n$',sst,re.M|re.I)           # check multiple lines(line ending with 'n')
print(e)                                 
