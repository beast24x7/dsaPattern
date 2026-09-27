employees = [
    ("Ravi","IT"),
    ("John","HR"),
    ("Sam","IT"),
    ("Mike","Finance")
]

d = {}
for key,value in employees:
    d.setdefault(value,[]).append(key)

print(d)


words = [
    "cat",
    "dog",
    "apple",
    "banana"
]

d1 = {}

for i in words:
    d1.setdefault(len(i),[]).append(i)

print(d1)