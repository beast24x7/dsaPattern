n = 123

def largestNumber(n:int):
    arr = []
    while n > 0:
        digit = n % 10
        arr.append(digit)
        n = n // 10

    l = sorted(arr,reverse=True)

    return "".join(map(str,l))

print(largestNumber(123))

l = [3,30,34,5,9]

s = "".join(map(str,l))
print(s)
l = sorted([int(x) for x in s],reverse=True)
print("".join(map(str,l)))



