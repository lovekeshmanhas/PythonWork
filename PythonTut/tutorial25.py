# *args and **kwargs

def function_name_print(a, b, c, d):
    print(a, b, c, d)

# function_name_print("lovekesh", "manhas", "arun", "manit")

def funcArgs(passParam, *args, **kwargs): # *args and **kwargs should be the last passing parameter in function
    # print(args[0])
    print(type(args))
    print(passParam)
    for name in args:
        print(name)
    for key, value in kwargs.items():
        # print(key, value)
        print(f"{key} is a {value}")

values = ["lovekesh", "manhas"]
# funcArgs(values)
kValues = {"lovekesh":"Monitor", "manhas":"Programmer"}
funcArgs("Test pass value", *values, **kValues)