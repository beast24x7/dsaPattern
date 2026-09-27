def reverseNumber(n:int):
    n1 = 0
    while n > 0:
        digit = n % 10
        n1 = n1 * 10 + digit
        n = n // 10
    return n1
print(reverseNumber(123))
