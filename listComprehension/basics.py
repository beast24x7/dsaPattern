
num = []

def generate():
    for i in range(0,6):
        num.append(i)
    return num

print(generate())

print([x for x in range(0,6)])

square = [x*x for x in range(0,6)]
print()