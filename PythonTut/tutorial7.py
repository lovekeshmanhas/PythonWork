# if else

var1 =8
var2 = 24

"""
var3 = int(input())

if var3>var2:
    print("greater")
elif var3==var2:
    print("equal")
else:
    print("lesser")
"""

list1 = [5,7,4]
if 5 in list1:
    print("Yes 5 is in list")

if 24 not in list1:
    print("24 is not in list")

# input your age and find driving eligibility
# 18+ can drive
print("Enter your age")
age = int(input())
if age > 18:
    print("You are eligible for driving")
elif age == 18:
    print("Verify eligibility by personal examination")
else:
    print("You are not eligible for driving")