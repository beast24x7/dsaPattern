square = lambda x: x*x
print(square(5))

add = lambda a,b: a+b
print(add(5,4))

cube = lambda x: x*x*x


employees = [
    ("John", 50000),
    ("Sam", 60000),
    ("Mike", 40000)
]
print(sorted(employees,key=lambda x:x[1],reverse=True))

employees = [
    {"name":"John","salary":50000},
    {"name":"Sam","salary":70000},
    {"name":"Mike","salary":60000}
]

print(sorted(employees,key=lambda x:x["salary"],reverse=True))

nums = [1,2,3,4]
print(list(map(square,nums)))

print(list(map(lambda x:x*x*x,nums)))

print(list(filter(lambda x:x%2 == 0, nums)))

from functools import reduce

print(reduce(lambda x,y: x*y,nums))

employees = [
    ("John", "IT", 50000),
    ("Sam", "HR", 60000),
    ("Mike", "IT", 40000)
]

print(sorted(employees,key=lambda x:x[2]))

data = {
    "John":50000,
    "Sam":70000,
    "Mike":60000
}

print(max(data.items(),key=lambda x:x[1]))

names = [
    "John",
    "Christopher",
    "Sam"
]
print(sorted(names,key=len, reverse=True))