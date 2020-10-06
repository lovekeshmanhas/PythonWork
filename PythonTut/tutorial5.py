#Dictionary: key value pairs

dict = {}
print(type(dict))

dict1 = {"Lovekesh":"Veg", "Arun":"nonVeg", "Ajay":"Vegan"}
print(dict1["Arun"])

dict1 = {"Lovekesh":"Veg", "Arun":"nonVeg", "Ajay":"Vegan",
         "Manit":{"B":"10 roti", "L":"Roti rice","D":"5kg Chicken"}}
print(dict1["Manit"])
print(dict1["Manit"]["L"])

dict1["Amit"]="German food"
print(dict1["Amit"])

del dict1["Manit"]  # delete manit record
print(dict1)

dict2 = dict1  # share same reference object address. change in dict2 also impact on dict1
print(dict2)

dict2 = dict1.copy() # return copy of reference object, change in dict2 does not impact on dict1

dict1.update({"Manhas":"IceCream"})
print(dict1)

print(dict1.keys())

print(dict1.items())


