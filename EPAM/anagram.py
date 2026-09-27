
def isAnagram(s,s1):
    return sorted(s) == sorted(s1)



print(isAnagram("abc","cbaa"))