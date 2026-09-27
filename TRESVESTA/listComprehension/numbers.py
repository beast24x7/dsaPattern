
print([x for x in range(1,10) if x % 2 == 0])
print([x for x in range(1,10) if x % 2 != 0])

print(["even" if x % 2 == 0 else "odd" for x in range(1,10)])


matrix = [[1,2],[3,4],[5,6]]

def flatten(l:list): 
    lst = []
    for i in l:
        if isinstance(i,list):
            lst.extend(flatten(i))
        else:
            lst.append(i)
    return lst

print(flatten(matrix))


result = (x for x in range(0,6) if x > 1)

for i in result:
    print(i,end=",")

words = ["Spark", "", "Python", "", "Scala"]
#output= ["spark", "python", "scala"]

print([x.lower() for x in words if x])


nums = ["10", "20", "30", "40"]
print([int(x) for x in nums])