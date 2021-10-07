'''Method overriding : When we use parent class method in child class with some specific implementation '''
class bank:
    def getroi(self):
        print(7)
r = bank()
r.getroi()
class sbi(bank):
    def getroi(self):
        print(5)
a = sbi()
a.getroi()
