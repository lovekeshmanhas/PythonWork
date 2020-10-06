# files

f = open("AlphaFile.txt")
print(f.tell())  # info regarding the current file pointer
print(f.readline())
print(f.tell())
print(f.readline())
print(f.tell())
print(f.seek(0)) # reset pointer to passed value
print(f.readline())

f.close()