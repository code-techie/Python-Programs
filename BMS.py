class Account():
    def __init__(self,accntNo,accntName,accntBalance):
        self.accntNo=accntNo
        self.accntName=accntName
        self.accntBalance=accntBalance


b = Account(100, "saving", 5000)
a = Account(101, "saving", 5000)
c = Account(103, "saving", 5000)


def withamnt(self,accntNo,amnt):
    if amnt>self.accntBalance:
        print("Not enough Balance!")
    else:
        print(f'Updated balance of {self.accntNo} is:', self.accntBalance-amnt)

def depamnt(self,accntNo,amnt):
        print(f'Updated balance of {self.accntNo} is:', self.accntBalance+amnt)
withamnt(a, 101, 200)
depamnt(a, 101, 200)