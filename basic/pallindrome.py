def pallindrome(n: int):
    n1 = 0 
    temp = n
    while n > 0:
        digit = n % 10
        n1 = n1 * 10 + digit 
        n = n // 10

    return n1 == temp

print(pallindrome(121))




def pallindromeString(s:str):
    l = len(s) -1 
    s1 = ""
    for i in range(l,-1,-1):
        s1 = s1 + s[i]
    return s1 == s

print(pallindromeString("abc"))



s = "A man, a plan, a canal: Panama"

import re

s = re.sub(r'[^a-z0-9A-Z]','',s.lower())

l = len(s) - 1
s1 = ""
for i in range(l,-1,-1):
    s1 = s1 + s[i]
print(s1 == s)
