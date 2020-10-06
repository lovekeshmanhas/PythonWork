# single inheritance

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

class Programmer(Employee):
    def __init__(self, name, salary, role, lang):
        super(Programmer, self).__init__(name, salary, role)
        self.lang = lang

    def printProg(self):
        return f"The Programmer's Name is {self.name}. Salary is {self.salary} and role is {self.role} and know language {self.lang}"

lovekesh = Employee("Lovekesh Manhas", 788, "Instructor")
arun = Employee("Arun", "876", "Manager")

manit = Programmer("Manit", 765, "Programmer", ["python"])
print(manit.printProg())