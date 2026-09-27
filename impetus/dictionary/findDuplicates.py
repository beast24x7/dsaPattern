def findDuplicates(s:str):
    d = {}
    for i in s:
        d[i] = d.get(i,0) + 1
    for k,v in d.items():
        if v == 2:
            print(k,v)

findDuplicates("abcdabcs")