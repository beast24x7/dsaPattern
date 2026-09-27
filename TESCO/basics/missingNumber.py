def find_missing(arr):
    n = len(arr) + 1

    xor = 0

    # XOR all numbers from 1 to n
    for i in range(1, n + 1):
        xor ^= i

    # XOR all numbers in array
    for num in arr:
        xor ^= num

    return xor


arr = [1, 2, 3, 5, 6]

#print(find_missing(arr))

def nSum(arr:list):
    n = len(arr)+1
    sum = (n*(n+1)) // 2
    c = 0
    for i in arr:
        c = c + i

    return (sum - c)


print(nSum([1,3,4,5]))