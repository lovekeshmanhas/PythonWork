# string operation
initialStr = "Python programming is best language for ML"
print(len(initialStr))
print(initialStr[0:6])
print(initialStr[:6])
print(initialStr[0:])
print(len(initialStr))

#print(initialStr[60])
print(initialStr[0:60])


print(initialStr[0:6:2])
print(initialStr[0::2])
print(initialStr[::2])

# negative indices
print(initialStr[-4:-1])

#reverse string
print(initialStr[::-1])

#String functions
print(initialStr.isalnum())  # alphanumeric number check
print(initialStr.isalpha())  # alphabetic check
print(initialStr.endswith("ML"))
print(initialStr.count("L"))
print(initialStr.capitalize())
print(initialStr.find("is"))
print(initialStr.lower())
print(initialStr.upper())
print(initialStr.replace("best", "excellent"))