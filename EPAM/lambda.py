

square = lambda x:x*x
print(square(6))

print(list(map(lambda x: x*x,[1,2,3,4,5])))

print(list(map(square,[1,2,3,4,5])))

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

print(sorted(employees, key=lambda employee: employee["salary"],reverse=True))

print(min(employees,key= lambda x:x["salary"]))

print(max(employees,key=lambda x: x["salary"]))

l = [1,2,3,4,5,6,7,8]

print(list(filter(lambda x:x % 2 ==0,l)))


from functools import reduce 

print(reduce(lambda x,y: x+y,l))

employees = [
    ("John", "IT", 50000),
    ("Sam", "HR", 60000),
    ("Mike", "IT", 40000)
]


print(sorted(employees,key=lambda x: (x[1],x[2]),reverse=True))