# Lambda functions

# def add(a,b):
#     return a+b
# 
# minus = lambda x, y: x-y
# 
#  def minus(a,b):
#      return a-b
# 
# print(minus(8,4))

# def a_first(a):
#     return a[1]

a = [[2,15],[4,6],[6,14]]
#a.sort(key=a_first)
a.sort(key=lambda x:x[1])
print(a)