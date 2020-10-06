# for loop

list1 = ["Lovekesh", "Arun", "Ajay", "Manit", "Amit"]

for item in list1:
    print(item)

list2 = ("Lovekesh", "Arun", "Ajay", "Manit", "Amit")

for item in list2:
    print(item)

list3 = [["Lovekesh", 1], ["Arun",4], ["Ajay",6], ["Manit",8], ["Amit",10]]

for item, rollnumber in list3:
    print(item, " rollnumber is ", rollnumber)

dict1 = dict(list3)
for item, rollnumber in dict1.items():
    print(item, " rollnumber is ", rollnumber)

for item in dict1:
    print(item)

#Exercise
#Create a list with any datatype
# print only numbers which is greater than 6
print("===================")
listData = ["lovekesh", 2, "Arun", 6 , "Manit", 8, 24.60]
for item in listData:
    if isinstance(item, (int, float)) and item > 6:
            print(item)

print("===================")
for item in listData:
    if str(item).isnumeric() and item > 6:
            print(item)