#class method

class Employee:
    no_of_leaves = 8

    def __init__(self, name, salary, role):
        self.name=name
        self.salary=salary
        self.role=role

    def printDetails(self):
        return f"Name is {self.name}. Salary is {self.salary} and role is {self.role}"

    @classmethod
    def changeLeaves(cls, newLeaves):
        cls.no_of_leaves = newLeaves


lovekesh = Employee("Lovekesh Manhas", 788, "Instructor")
arun = Employee("Arun", "876", "Manager")
lovekesh.changeLeaves(9)
print(lovekesh.printDetails())
print(arun.printDetails())


print(lovekesh.no_of_leaves)
print(arun.no_of_leaves)