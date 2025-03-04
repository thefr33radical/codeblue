

#Sort list of list
def myfunc(l):
    return l[1]
l = [[2, 3], [6, 7], [3, 34], [24, 64], [1, 43]]
l=sorted(l, key=myfunc,reverse=True)
print(l)

#Sort list of objects

class Custom(object):
    def __init__(self, name, number):
        self.name = name
        self.number = number
        self.__class__.__name__="gears"
        
    def __repr__(self):
        return "{} : {} {}".format(self.__class__.__name__,self.name,self.number)

l2 = [
    Custom('object', 99),
    Custom('michael', 1),
    Custom('theodore the great', 59),
    Custom('life', 42)]
def myfunc2(l2):
    return l2.number
l2=sorted(l2,key=myfunc2,reverse=True)
print(l2)
