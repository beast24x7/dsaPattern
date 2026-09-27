words = [
    "cat",
    "dog",
    "apple",
    "banana"
]

d = {}

for i in words:
    d.setdefault(len(i),[]).append(i)

print(d)


employees = [
    ("Ravi","IT"),
    ("John","HR"),
    ("Sam","IT"),
    ("Mike","Finance")
]


d1 = {}

for i,j in employees:
    d1.setdefault(j,[]).append(i)

print(d1)


employees = {
    101: {"name":"Ravi","salary":50000},
    102: {"name":"John","salary":70000},
    103: {"name":"Sam","salary":60000}
}


print(max(employees,key=lambda x:employees[x]["salary"]))



s = "aabbccddef"
dict = {}


for i in s:
    dict[i] = dict.get(i,0) + 1

print(dict)

for key,value in dict.items():
    if value == 1:
        print(key)
        break