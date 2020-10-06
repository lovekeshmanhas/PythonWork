# Functions

a = 4
b = 6
c = sum((a,b)) # build in function
print(c)

def function1():
    print("Hello function1")

print(function1())

# function with passing parameters
def function2(a, b):
    print("Sum of two numbers: ", a+b)

function2(10,8)

# function passing parameters with return
def function3(a, b):
    """Function to calculate average of two numbers"""
    average = (a+b)/2
    return average

avgValue = function3(10,8)
print(avgValue)
print(function3.__doc__)  # doc string
print(sum.__doc__)