class Person:
    def __init__(self, name, id, age):
        self.name = name               # name is Public variable
        self._id = id                  # id is protected variable
        self.__age = age               # age is private variable
 
    def display(self):
        print(self.name)
        print(self._id)
        print(self.__age)

 
person = Person('Dev', "Adhar",20)
person.display()      # accessing private variable is possible using class method
    

print(person.name)
print(person._id)    # can be accessed using the scope of class
print(person.__age)  # private variable cannot be accessed directly from the outside class