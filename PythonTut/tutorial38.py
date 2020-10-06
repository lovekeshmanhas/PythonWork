# static methods

class Employee:
    no_of_leaves = 8

    def __init__(self, name, salary, role):
        self.name=name
        self.salary=salary
        self.role=role

    def printDetails(self):
        return f"Name is {self.name}. Salary is {self.salary} and role is {self.role}"

    #class method
    @classmethod
    def changeLeaves(cls, newLeaves):
        cls.no_of_leaves = newLeaves

    # alternative method
    @classmethod
    def from_str(cls, string):
        # params = string.split("-")
        # return cls(params[0],params[1], params[2])
        return cls(*string.split("-"))

    # static method
    @staticmethod
    def printStatic(str):
        print("This is static", str)

lovekesh = Employee("Lovekesh Manhas", 788, "Instructor")
arun = Employee("Arun", "876", "Manager")
manit = Employee.from_str("Manit-678-Prin")

print(lovekesh.printDetails())
print(arun.printDetails())
print(manit.printDetails())

Employee.printStatic("Test")
