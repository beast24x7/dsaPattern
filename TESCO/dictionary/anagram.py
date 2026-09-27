def anagram(s1:str, s2:str):
    d1 = {}
    d2 = {}
    if len(s1) != len(s2):
        return False
    else:
        for i in s1.lower():
            d1[i] = d1.get(i,0) + 1
        for i in s2.lower():
            d2[i] = d2.get(i,0) + 1

    return d1 == d2

print(anagram("Listen","Silent"))   