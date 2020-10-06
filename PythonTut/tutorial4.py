#List in python
# list is mutable
grocery = ["Harpic", "Vim", "Deodrant", "Lady Finger", "Lollypop", 35]
print(grocery)
print(grocery[3])

numbers = [4,8,2,6,9,18]
print(numbers)
print(numbers[3])

numbers.sort()
print(numbers)

numbers.reverse()
print(numbers)

#Slicing
print(numbers[2:5])  # returns a list

print(numbers[::2])

print(numbers[::-1]) # always use -1, not less than that

print(len(numbers))
print(max(numbers))
print(min(numbers))

# append numbers in list
numbers.append(24)
numbers.append(87)
print(numbers)

# insert numbers
numbers.insert(4,99)
print(numbers)

#remove
numbers.remove(99)
print(numbers)

#pop: to remove last element
numbers.pop()
print(numbers)

# change index value
numbers[2] = 88
print(numbers)

tp = (1,3,6)
print(tp)

#tp[1] = 7   # tuple object is immutable

tp1 = (1,) # put , in case of one element for tuple
print(tp1)

#swap numbers
a = 8
b = 4
a,b = b,a
print(a,b)
