def anagram(s1:str,s2: str)-> bool :
    dict1 = {}
    dict2 = {}
    if len(s1) != len(s2):
        return False
    else:
        for s in s1.lower():
            dict1[s] = dict1.get(s,0) + 1
        for s in s2.lower():
            dict2[s] = dict2.get(s,0) + 1  

        if dict1 == dict2:
            return True
        else:
            return False
        

print(anagram("abc","cbaa"))