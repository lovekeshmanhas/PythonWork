#break and continue
"""
i=0
while(i<24):
    if i > 5:
        continue
    print(i+1, end=" ")
    if i == 24:
         break
    i = i+1
"""
#Exercise
while(True):
   inputNumber = int(input("Enter a number"))
   if inputNumber > 100:
       print("Great number is greater than 100")
       break
   else:
       print("Try again\n")
       continue