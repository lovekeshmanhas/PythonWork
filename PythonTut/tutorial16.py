# file read

f = open("AlphaFile.txt", "rt")  # default is rt
# content = f.read()
# print(content)

# content = f.read(3)
# print(content)
#
# content = f.read(344)
# print(content)

# Read line wise
# for line in f:
#     print(line)
# print(f.readline())
# print(f.readline())

print(f.readlines())
f.close()