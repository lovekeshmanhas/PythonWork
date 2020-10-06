# file write
f = open("AlphaFile.txt","w")
f.write("file is open in write mode")
f.close()

# file append
f = open("AlphaFile.txt","a")
a= f.write("\nfile is open in append mode")
print(a)
f.close()

#file read and write
f = open("AlphaFile.txt","r+")
print(f.read())
f.write("\nfile is open in read and write mode")
f.close()