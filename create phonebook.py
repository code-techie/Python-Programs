class create_dict(dict):
    def __init__(self):
        self = dict()
        self[key]=value
    def add(self, key, value):
        self[key] = value
dct = create_dict()
dct.add('a', 19)
dct.add('b', 21)
print(dct)