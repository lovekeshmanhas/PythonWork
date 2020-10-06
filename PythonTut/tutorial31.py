# Map, filter, reduce

numbers = ["4", "24", "16"]

numbers = list(map(int, numbers))

# for i in range(len(numbers)):
#     numbers[i] = int(numbers[i])

numbers[2] = numbers[2] + 1
print(numbers[2])

def sq(a):
    return a*a

num = [3,6,23,7,45]
square = list(map(sq, num))
print(square)

square1 = list(map(lambda x:x*x, num))
print(square1)

def cube(a):
    return a*a*a

func =[sq,cube]
for i in range(5):
    val = list(map(lambda x:x(i), func))
    print(val)

#========filter
lst1 = [1,2,4,5,6,7,8,9]
def is_greater_5(num):
    return num>5

grt_list = list(filter(is_greater_5, lst1))
print(grt_list)

#=============Reduce
from functools import reduce

lst2 = [1,2,3,4]
num=0
for i in lst2:
    num = num+i
print(num)

num = reduce(lambda x,y:x+y, lst2)
print(num)