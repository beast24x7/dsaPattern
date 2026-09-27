from typing import List
def binarySearch(arr: List[int], target: int) -> int:

    low, high = 0, len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1


print(binarySearch([0,1,2,3,4,5,8,81], 5))
print(binarySearch([1,2,3,4,5,6,7], 7))


def binarySearch1(arr:list, target:int):
    start, end = 0, len(arr) -1 
    while start <= end:
        mid = (start+end)//2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            start = mid + 1
        else:
            high = mid -1 
    return -1 


print(binarySearch1([0,1,2,3,4,5,8,81], 5))
print(binarySearch1([1,2,3,4,5,6,7], 7))