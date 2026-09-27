employees = [
    ("Ravi","IT"),
    ("John","HR"),
    ("Sam","IT"),
    ("Mike","Finance")
]

dict = {}
for key,values in employees:
    dict.setdefault(values,[]).append(key)

print(dict)