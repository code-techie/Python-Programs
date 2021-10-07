dict = {"bhu":123,"he":456}
# adding key-value pair in dictionary
dict.update({"em":745})
# check key exist in dictionary or not
'''
for i in list(dict.keys()):
    if "df" in list(dict.keys()):
        print(True)
        break
        print(False)
        break
'''
# deleting key-value pair in dictionary
del dict["he"]
stu = dict.copy()
print(stu)
st = list(dict.keys())
st.sort()
print(st)
for S in st:
      print(":".join((S,str(dict[S]))))
print(S)
print(len(dict))
print(str(dict))
print("ze"in dict)