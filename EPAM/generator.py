

def generateSequence(n):

    for _ in range(n):
        yield _

x = generateSequence(5)

print(next(x))
print(next(x))
print(next(x))


def generateSequence1(n):
    return (x for x in range(n))

x1 = generateSequence1(5)


for i in x1:
    print(i)



def fibonacci(r):
    a,b = 0,1
    for i in range(r):
        yield a
        a,b = b,a+b
        
result = fibonacci(6)

for i in result:
    print(i)

def readFile(filename):
    with open(filename,"r") as fp:
        for line in fp:
            yield line.strip()

data = readFile("resources/log.txt")

for i in data:
    print(i)
