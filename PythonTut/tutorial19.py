# file with block
with open("AlphaFile.txt") as f:
    a = f.readlines()
    print(a)


f = open("AlphaFile.txt", "rt")
# print(f.readlines())
print(f.readline())
f.close()