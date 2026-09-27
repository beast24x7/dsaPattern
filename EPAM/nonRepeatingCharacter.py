d = {}
def nonRepeatingCharacter(s:str):
    for i in s:
        d[i] = d.get(i,0) + 1 
    print(d)
    return min(d.items(),key= lambda x: x[1]) 


d1 = {}
def nonRepeatingChar(s: str):
    for i in s:
        d1[i] = d1.get(i,0) + 1
    for i in s:
        if d1[i] == 1:
            return i





print(nonRepeatingCharacter("abbabacde"))

print(nonRepeatingChar("abbac"))