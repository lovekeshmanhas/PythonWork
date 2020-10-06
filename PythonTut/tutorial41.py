# Multiple inheritance

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

class Player:
    no_of_games = 4
    def __init__(self, name, game):
        self.name = name
        self.game = game

    def printdetails(self):
        return f"Name is {self.name}. Game is {self.game}"

class CoolProgrammer(Employee, Player):
    language = "C++"
    def printLanguage(self):
        print(self.language)


lovekesh = Employee("Lovekesh Manhas", 788, "Instructor")
arun = Employee("Arun", "876", "Manager")

manit = Player("Manit", ["Cricket"])
ajay = CoolProgrammer("Ajay", 8934, "CoolProgrammer")
print(ajay.printdetails())
