def rotateVowels(s:str):
    left, right = 0, len(s)-1
    s = list(s)
    while left < right:
        if s[left] and s[right] in ("a","e","i","o","u"):
            s[left],s[right] = s[right],s[left]
            left +=1
            right -=1
        return "".join(s)

print(rotateVowels("abcde"))


