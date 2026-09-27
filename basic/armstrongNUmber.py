
def armstrongNumber(n:int):
    total = 0
    temp = n
    while temp > 0:
        digit = temp % 10
        total = total + digit ** 3
        temp //= 10
    return (n == total)

print(armstrongNumber(153))


