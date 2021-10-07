class Person:
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname

    def printname(self):
        print(f'My name is {self.fname} and Sirname is {self.lname}\n')


a = Person("Bhushan", "Deulkar")


class student(Person):
    def __init__(self, fname, lname, age, year):
        self.age = age
        self.year = year
        super().__init__(fname, lname)

    def printname(self):
        print(f'My name is {self.fname} and Sirname is {self.lname}  and age is {self.age} yrs old and year is {self.year}\n')


class employee(student):
    def __init__(self, fname, lname, age, year, salary, id):
        self.salary = salary
        self.id = id
        super().__init__(fname, lname, age, year)

    def printname(self):
        print(f'\nMy name is {self.fname} and Sirname is {self.lname} age is {self.age} yrs old and YoB {self.year} and salary is {self.salary} and id is {self.id}')


a = Person('Bhushan', 'Deulkar')
b = student('juma', 'mukund', 21, 1996)
c = student('gaer', 'rukta', 27, 1992)
d = employee('Bhushan', 'Deulkar', 25, 1996, 40000, 101)
a.printname()
b.printname()
c.printname()
d.printname()
