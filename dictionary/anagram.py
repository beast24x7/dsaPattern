def anagram(str1,str2):
    dict1 = {}
    dict2 = {}
    if len(str1) != len(str2):
        return False
    else:
        for s in str1.lower():
            dict1[s] = dict1.get(s,0) + 1
        for s1 in str2.lower():
            dict2[s1] = dict2.get(s1,0) + 1
        if dict1 == dict2:
            return True
        else: 
            return False


print(anagram("Listen","Silent"))   
