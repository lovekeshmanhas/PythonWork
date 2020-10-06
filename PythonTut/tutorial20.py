# Scope, Global keyword and variable

l = 10 # Global variable
def function1(n):
    #l = 5  # local variable
    k = 6  # local variable
    global l   # Without global keyword, l does not change
    l = l + 45
    print(n, "Printed")
    print(l,k)

function1("I ")
print(l)

def function2():
    x = 20
    def test():
        global x
        x = 60
    print("Before calling test() ", x)
    test()
    print("After calling test() ", x)

function2()
print(x)