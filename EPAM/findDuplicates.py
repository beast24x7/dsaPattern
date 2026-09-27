input=[1,2,3,2,4,5,1]
d ={}
def duplicate(l:list):
    for i in l:
        d[i] = d.get(i,0) + 1
    s = set()
    for i in l:
        if d[i] == 2:
            s.add(i)
    return s

print(duplicate(input))