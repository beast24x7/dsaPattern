

def occurence(s: str):
    d = {}
    for i in s:
        d[i] = d.get(i,0)+1
    return d

print(occurence("abcdefghabcfs"))
