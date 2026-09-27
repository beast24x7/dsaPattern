def armstrong(num:int):
    n = 0
    temp = num
    while num > 0:
        digit = num % 10
        n = n + digit ** 3
        num = num // 10
    return (n == temp)

print(armstrong(153))


