def square():
    for i in range(6):
        yield i*i

g = square()

for i in range(6):
    print(next(g))