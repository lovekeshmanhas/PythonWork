# setter

class Employee:
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname
        #self.email = f"{fname} {lname} @test.com"

    def explain(self):
        return f"This employee is {self.fname} {self.lname}"

    @property
    def email(self):
        if self.fname == None or self.lname == None:
            return "Email not set, Please use setter to set"
        return f"{self.fname} {self.lname} @test.com"

    @email.setter
    def email(self, str):
        names = str.split("@")[0]
        self.fname = names.split(".")[0]
        self.lname = names.split(".")[1]

    @email.deleter
    def email(self):
        self.fname = None
        self.lname = None

emp1 = Employee("Lovekesh", "Manhas")
emp2 = Employee("Arun", "Kumar")

print(emp1.explain())
print(emp1.email)

emp1.fname = "Love"
print(emp1.email)
emp1.email = "testf.testl@test.com"
print(emp1.fname)
print(emp1.lname)
print(emp1.email)

del emp1.email
print(emp1.email)