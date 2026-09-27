employees = [
    ("Ravi","IT"),
    ("John","HR"),
    ("Sam","IT"),
    ("Mike","Finance")
]

def groupEmployees(emp:dict):
    d = {}
    for key,value in emp:
        d.setdefault(value,[]).append(key)
    return d

print(groupEmployees(employees))

words = [
    "cat",
    "dog",
    "apple",
    "banana"
]

d = {}
for i in words:
    d.setdefault(len(i),[]).append(i)
