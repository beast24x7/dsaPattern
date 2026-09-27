from typing import List

def sorting(arr: List[int]) -> List[int]:
    n = len(arr)
    for i in range(n):
        for j in range(n-i-1):
            if arr[j] > arr[j+1]:
                arr[j],arr[j+1] = arr[j+1],arr[j]
    return arr

print(sorting([9,3,5,1,8,3,2]))


def sorting(arr:list):
    l = len(arr)
    for i in range(0,l):
        for j in range(0,l-i-1):
            if arr[j] > arr[j+1]:
                arr[j],arr[j+1] = arr[j+1],arr[j]

    return arr

print(sorting([2,1,0,4,9,3]))