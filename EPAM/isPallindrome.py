def isPallindrome(s: str) -> bool:
    return s == s[::-1]


print(isPallindrome("abba"))