class Vehicle:

    def __init__(self, name, color, price):
        self.name = name
        self.color = color
        self.price = price

    def show(self):
        print('Details:', self.name, self.color, self.price)

    def max_speed(self):
        print('Vehicle max speed is 150')

    def change_gear(self):
        print('Vehicle change 6 gear')


# inherit from vehicle class

class Car(Vehicle):
    def max_speed(self):
        print('Car max speed is 240')

    def change_gear(self):
        print('Car change 7 gear')

c1 = Car("bmw", "black", 50)
c1.max_speed()

# Car Object
c1 = Car('Car x1', 'Red', 20000)
c1.show()
# calls methods from Car class
c1.max_speed()
c1.change_gear()

# Vehicle Object
v1 = Vehicle('Truck x1', 'white', 75000)
v1.show()
# calls method from a Vehicle class
v1.max_speed()
v1.change_gear()