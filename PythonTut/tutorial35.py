#Self and __init__ constuctor

class Employee:
    no_of_leaves = 8

    def __init__(self, name, salary, role):
        self.name=name
        self.salary=salary
        self.role=role

    def printDetails(self):
        return f"Name is {self.name}. Salary is {self.salary} and role is {self.role}"


lovekesh = Employee("Lovekesh Manhas", 788, "Instructor")
arun = Employee("Arun", "876", "Manager")

# lovekesh.name = "Lovekesh Manhas"
# lovekesh.salary = 664
# lovekesh.role = "Instructor"
#
# arun.name = "Arun Kumar"
# arun.salary = 728
# arun.role = "Student"

print(lovekesh.printDetails())
print(arun.printDetails())

print(lovekesh.no_of_leaves)