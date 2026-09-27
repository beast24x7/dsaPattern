print([x for x in range(0,10)])

print([x for x in range(0,10) if x % 2 == 0])

print([x for x in range(0,10) if x %2 != 0 ])



print(["Even" if x % 2 == 0 else "Odd" for x  in range(0,10)])

print([x*x for x in range(0,10)])

result = (x*x for x in range(0,10))

for i in result:
    print(i,end=" ")


words = ["Spark", "", "Python", "", "Scala"]
#output= ["spark", "python", "scala"]

print([x.lower() for x in words if x])


nums = ["10", "20", "30", "40"]

print([int(i) for i in nums])

names = ["ravi", "john", "sam"]

print([x.upper() for x in names])