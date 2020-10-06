# Operator overloading and Dunder method

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

    def __add__(self, other):
        return  self.salary + other.salary

    def __truediv__(self, other):
        return  self.salary / other.salary

    def __repr__(self):
        return  f"Employee ('{self.name}', {self.salary} , '{self.role}')"

    def __str__(self):
        return  self.printDetails()

emp1 = Employee("Lovekesh", 876, "Programmer")
emp2 = Employee("Arun", 2763, "Analyst")

print(emp1 + emp2)
print(repr(emp1))
print(emp1)

