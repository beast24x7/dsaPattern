

def reverseString(s: str) -> str:
    return s[::-1]

print(reverseString("abc"))

def reverse_string(s):
    result = ""

    for ch in s:
        result = ch + result

    return result

print(reverse_string("abc"))