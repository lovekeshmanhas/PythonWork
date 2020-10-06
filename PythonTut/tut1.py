import sklearn

def func1(string):
    return f"test the string pass {string}"

def add(num1, num2):
    return num1 + num2 + 5

print("func name ", __name__)

if __name__ == '__main__':
    print(func1("Lovekesh"))
    sum = add(2,6)
    print(sum)