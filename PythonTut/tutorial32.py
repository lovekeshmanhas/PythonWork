# Decorators

def func1():
    print("Test now")

func2 = func1
del func1
func2()


def outFunc(num):
    if num==0:
        return print
    if num==1:
        return sum

a = outFunc(1)
print(a)


def executor(func):
    func("this")

executor(print)

# Decorators
def dec1(func1):
    def nowexec():
        print("Excecution now")
        func1()
        print("Executed")
    return nowexec

@dec1
def infoReturn():
    print("Python programming")

#infoReturn = dec1(infoReturn)
infoReturn()

