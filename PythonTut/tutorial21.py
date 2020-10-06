# Recursion: Recursive vs iterative

# def print2(str1):
#     print2(str1)
#     print("This is " + str1)
#
# print2("Recursive error")

def factorial_iterative(n):
    """
    :param n:
    :return: n * n -1 * n -2 * n - 3.......1
    """
    fac = 1
    for i in range(n):
        fac = fac * (i+1)
    return fac

def factorial_recursive(n):
    """
    :param n:
    :return: n * n -1 * n -2 * n - 3.......1
    """
    if n == 1:
        return 1
    else:
        return n * factorial_recursive(n-1)

number = int(input("Enter the number "))
print("Factorial calculation using iterative method ", factorial_iterative(number))
print("Factorial calculation using recursive method ", factorial_recursive(number))

def fibonacci(n):
    """
    :param n:
    :return:
    """
    if n == 0:
        return 1
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

print("Fibonacci calculation using recursive method ", fibonacci(number))
