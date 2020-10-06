# Class and object 2
class Employee:
    no_of_leaves = 8
    pass

lovekesh = Employee()
arun = Employee()

lovekesh.name = "Lovekesh Manhas"
lovekesh.salary = 664
lovekesh.role = "Instructor"

arun.name = "Arun Kumar"
arun.salary = 28
arun.role = "Student"

print(lovekesh.name, lovekesh.no_of_leaves)
print(Employee.__dict__)
arun.no_of_leaves = 9
print(arun.__dict__)