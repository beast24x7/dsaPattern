n = 36
result = []
for i in range(1,37):
    if n % i == 0:
        result.append(i)

print(result)


def gcd(n1,n2):
    while n2 != 0:
        n1,n2 = n2, n1 % n2
    return n1


print(gcd(9,12))

def gcd(a, b):
    while b != 0:
        a, b = b, a % b

    return a


print(gcd(48, 18))