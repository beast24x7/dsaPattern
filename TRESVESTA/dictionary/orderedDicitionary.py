d = {
    "A": 50,
    "B": 20,
    "C": 80,
    "D": 10
}

l = len(d.items())
lst = list(d.items())

for i in range(0,l):
    for j in range(0,l-i-1):
        if lst[j][1] > lst[j+1][1]:
            lst[j],lst[j+1] = lst[j+1],lst[j]

        
print(lst)

print(sorted(d.items(),reverse= True))