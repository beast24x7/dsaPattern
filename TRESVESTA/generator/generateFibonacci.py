
def generateFibonacci():
    a = 0
    b = 1
    for i in range(0,100):
        yield  a
        a,b = b, a+b

result = generateFibonacci()

for i in range(0,5):
    print(next(result))