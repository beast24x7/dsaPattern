"""
Left Rotate by 1
Before:
1 2 3 4 5

After:
2 3 4 5 1

Right Rotate by 1
Before:
1 2 3 4 5

After:
5 1 2 3 4
"""

1,2,3,4,5
5,4,3,2,1
2,3,4,5,1

def reverse(arr, left, right):
    while left < right:
        arr[left], arr[right] = arr[right], arr[left]
        left += 1
        right -= 1

arr = [1,2,3,4,5]
k = 2

n = len(arr)
#k %= n

reverse(arr, 0, k-1)
reverse(arr, k, n-1)
reverse(arr, 0, n-1)

print(arr)