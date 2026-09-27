d = {
    "A": 50,
    "B": 20,
    "C": 80,
    "D": 10
}

l = len(d)
item = list(d.items())
for i in range(0,l):
    for j in range(0,l-i-1):
        if item[j][1] < item[j+1][1]:
            item[j],item[j+1] = item[j+1],item[j]

print(item)



