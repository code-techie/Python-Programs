class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def intro(self):
        return print(f"Name is {self.name} and age is {self.age}")

class Employee(Person):

    def __init__(self, name, age,company):
        self.company=company
        super().__init__(name,age)

    def getcompany(self):
        return print(f"{self.name} is working in {self.company}")


e1 =Employee("Bhushan",25, "TCS")

e1.getcompany()
e1.intro()

p1 = Person("Mohan", 21)
p1.intro()

    