# Time module
import time

t = time.time()
print(t)
i=0
while (i<5):
    print("test performance")
    i+=1

print("while loop time in", time.time() - t)

t2 = time.time()
for i in range(5):
    # time.sleep(1)
    print("test performance")

print("For loop time in", time.time() - t2)

localtime = time.asctime(time.localtime(time.time()))
print(localtime)