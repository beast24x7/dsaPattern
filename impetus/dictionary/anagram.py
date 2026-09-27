def anagram(s:str,s1:str):
    if len(s) != len(s1):
        return False
    else:
        d1 = {}
        d2 = {}
        for i in s:
            d1[i] = d1.get(i,0)+1
        for i in s1:
            d2[i] = d2.get(i,0)+1
        if d1 == d2:
            return True
        else: 
            return False

print(anagram("abc","cbaa"))

