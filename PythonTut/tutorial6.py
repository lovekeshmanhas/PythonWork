# Set

s = set()
print(type(s))

set_from_list = set([2,4,6,8])
print(set_from_list)
print(type(set_from_list))

s.add(1)
s.add(1) #set only add unique values
print(s)

s.add(2)
print(s)

s1 = s.union({1,3,5})
print(s, s1)

s1 = s.intersection({1,3,5})
print(s, s1)

print(s.isdisjoint(s1))

s.remove(2)
print(s)