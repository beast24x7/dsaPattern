def pallindrome(n:int):
    temp = n
    num = 0
    while n > 0:
        digit = n % 10
        num = num * 10 + digit
        n = n // 10
    return temp == num


print(pallindrome(1212))


def pallindromeString(s:str):
    temp = ""
    for i in range(len(s)-1,-1,-1):
        temp = temp + s[i]
    return temp == s


print(pallindromeString("aba"))


s = "A man, a plan, a canal: Panama"

def pallindromeText(s:str):
    import re

    s = re.sub(r'[^a-z0-9A-Z]',"",s).lower()

    s1 = s[::-1]

    return s == s1


print(pallindromeText(s))
