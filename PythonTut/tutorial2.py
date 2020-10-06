#Variable, DataType, Typecasting
var1 = "hello world"
print(var1)

var2= 4;
var3= 36.7
print(type(var1))
print(type(var2))
print(type(var3))

print(var2 + var3)
#print(var1 + var2)


var4= " welcome"
print(var1 + var4)

#Typecast
var5= "24"
var6= "14"
print(int(var5) + int(var6))

print(10 * var1)

# input user input
print("Enter your number")
inpNum = input();
print("Your enterned number: ", inpNum);
print("Mutliple with 10: ", int(inpNum)*10);

# Addition of two number
print("Enter first number")
numFirst = input()
print("Enter second number")
numSecond = input()
print("Addition of two number: ", int(numFirst) + int(numSecond))