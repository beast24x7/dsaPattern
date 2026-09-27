
square = lambda x: x*x
print(square(5))

add = lambda a,b: a+b
print(add(4,5))

employees = [
    ("John", 50000),
    ("Sam", 60000),
    ("Mike", 40000)
]

s = sorted(employees,key = lambda employee:employee[1],reverse= True )
print(s)

employees = [
    {"name":"John","salary":50000},
    {"name":"Sam","salary":70000},
    {"name":"Mike","salary":60000}
]

s = sorted(employees,key = lambda emp: emp["salary"], reverse=True)

print(s)

print(max(employees,key=lambda emp: emp["salary"]))
print(min(employees,key= lambda x: x["salary"]))


nums = [1,2,3,4]

print(list(map(square,nums)))

print(list(map(lambda x: x*x, nums)))

print(list(filter(lambda x: x%2 == 0,nums)))


from functools import reduce

print(reduce(lambda x,y: x +y, nums))


employees = [
    ("John", "IT", 50000),
    ("Sam", "HR", 60000),
    ("Mike", "IT", 40000)
]

print(sorted(employees,key=lambda x: (x[1],x[2])))

data = {
    "John":50000,
    "Sam":70000,
    "Mike":60000
}

highest_salary = max(data.items(), key=lambda x: x[1])

print(highest_salary)
print(data)

names = [
    "John",
    "Christopher",
    "Sam"
]

largestString = sorted(names, key=lambda x: len(x),reverse=True)
print(largestString)