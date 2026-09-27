

print([x for x in range(0,11) if x % 2 == 0])

print([x for x in range(0,11) if x % 2 != 0])

print(["Even" if x % 2 == 0 else "Odd" for x in range(0,11)])

#flatten list 
matrix = [[1,2],[3,4],[5,6]]

print([number for row in matrix for number in row])

#list comprehension

print([x*x for x in range(0,6)])

#generator comprehension

result = (x*x for x in range(0,6))
for i in result:
    print(i,end=" ")

words = ["Spark", "", "Python", "", "Scala"]
#output= ["spark", "python", "scala"]

print([x.lower() for x in words if x])


nums = ["10", "20", "30", "40"]

print([int(x) for x in nums])