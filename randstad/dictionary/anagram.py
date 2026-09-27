def anagram(str1:str,str2:str):
    d = {}
    d1 = {}
    if len(str1) != len(str2):
        return False
    else:
        for i in str1:
            d[i] = d.get(0,1) + 1
        for i in str2:
            d1[i] = d.get(0,1) + 1
        if d == d1:
            return True
        else:
            return False
        


print(anagram("abc","bba"))