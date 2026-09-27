
print([x*x  for x in range(1,11)])

print([x*x*x for x in range(1,11)])

print([x for x in range(1,11) if x % 2 == 0])

print([x for x in range(1,11) if x % 2 != 0])

print(["Even" if x % 2 == 0 else "Odd" for x in range(1,11)])

x = (x for x in range(1,11))

for i in x:
    print(i,end=" ")

words = ["Spark", "", "Python", "", "Scala"]
#output= ["spark", "python", "scala"]

print([x.lower() for x in words if x ])

nums = ["10", "20", "30", "40"]

print([int(x) for x in nums])
