# F strings and String formatting
import math
me = "Lovekesh"
a1 = 3
# a = "This is %s %s"%(me, a1)
# a = "This is {1} {0}"
# b = a.format(me, a1)
# print(b)
a= f"this is {me} {a1} {4*65} {math.cos(65)}"
print(a)