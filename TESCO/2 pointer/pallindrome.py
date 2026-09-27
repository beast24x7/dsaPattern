def validPallindrome(s:str):

    import re
    s = re.sub(r'[^A-Z0-9a-z]',"",s)
    i,j = 0, len(s)-1
    
    while i < j:
        if s[i] != s[j]:
            return False
        i += 1
        j -= 1
        return True

print(validPallindrome("ab,cba,"))


