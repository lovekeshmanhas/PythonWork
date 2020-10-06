# Public, Priviate, Protected Access specifiers

# single inheritance

class Employee:
    no_of_leaves = 8
    _protec = 4
    __privt = 12

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


emp = Employee("Lovekesh Manhas", 788, "Instructor")

print(emp._protec)
print(emp._Employee__privt)
