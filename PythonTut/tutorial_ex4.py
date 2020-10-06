# Pattern Printing
"""
Input = Integer n
Boolean = True or False

True
*
**
***
****

False
****
***
**
*

"""
def ascendingPattern(numValue):
    pValue = 1
    while(pValue <= numValue):
        count = 1
        while(count <= pValue):
            print("*", end=" ")
            count = count + 1
        pValue = pValue + 1
        print()

def decendingPattern(numValue):
    pValue = 1
    while(numValue >= pValue):
        count = numValue
        while(count >= pValue):
            print("*", end=" ")
            count = count - 1
        numValue = numValue - 1
        print()

numValue = int(input("Enter the number"))
inputValue = int(input("Enter pattern value 1 for ascending 2 for descending"))
flagValue = True
if inputValue is 1:
    flagValue = True
else:
    flagValue = False

if flagValue:
    ascendingPattern(numValue)
else:
    decendingPattern(numValue)