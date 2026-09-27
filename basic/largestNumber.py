n = 123
def largestNumber(n: int):
    l = []
    while n > 0:
        digit = n % 10
        l.append(digit)
        n = n // 10
    l = sorted(l,reverse=True)

    return "".join(map(str,l))

print(largestNumber(654321))

from functools import cmp_to_key
l = [3,30,34,5,9]

l = [str(x) for x in l]

def compare_x_y(x,y):
    if x+y > y+x:
        return -1
    elif x+y < y+x:
        return 1
    else:
        return 0

l = sorted(l,key=cmp_to_key(compare_x_y))

print("".join(map(str,l)))
