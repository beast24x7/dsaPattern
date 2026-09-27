

def generateSequence():
    for i in range(0,100):
        yield i

result = generateSequence()

for i in range(0,10):
    print(next(result))
