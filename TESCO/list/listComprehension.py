
print([x for x in range(1,11)])

print(["even" if x % 2 == 0 else "odd" for x in range(1,11)])

print([x for x in range(1,11) if x % 2 == 0])

print([x for x in range(1,11) if x % 2 != 0])


names = ["ravi", "john", "sam"]


print([x.upper() for x in names])