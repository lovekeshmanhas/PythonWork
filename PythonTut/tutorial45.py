# Super() and Overriding in class

class A:
    clsVar1 = "I am a class variable in class A"
    def __init__(self):
        self.var1 = "I am inside class A's constructor"
        self.clsVar1 = "Instance var in class A"
        self.spcl = "Special variable"

class B(A):
    clsVar1 = "I am in class B"

    def __init__(self):
        super().__init__()
        self.var1 = "I am inside class B's constructor"
        self.clsVar1 = "Instance var in class B"

a = A()
b = B()

print(b.spcl,  b.clsVar1)