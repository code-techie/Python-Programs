phonebook = {}
num = int(input("enter number of contacts you want to add:"))
for i in range(0, num):
    name = str(input("enter name"))
    number = int(input("enter number"))
    phonebook[name] = number
for i in range(0, num):
    name = input("enter name")
    if name in phonebook:
        print(name + " = " + str(phonebook[name]))
    else:
        print("Not found")