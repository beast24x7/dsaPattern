
square = {x:x*x for x in range(1,6)}
print(square)


cube = {x: x*x*x for x in range(1,6)}
print(cube)

parityDict = {x: "even" if x % 2 == 0 else "odd" for x in range(1,10) if x>3}

print(parityDict)

dict = {
    "even": [x for x in range(1,10) if x %2 == 0],
    "odd": [x for x in range(1,10) if x % 2 != 0]
}

print(dict)