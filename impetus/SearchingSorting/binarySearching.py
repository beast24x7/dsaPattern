from typing import List

def binarySearch(arr: List[int], target: int):
    left, right = 0, len(arr) - 1

    while left <= right:
        mid = left + (right - left) // 2

        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1


print(binarySearch([1,2,3,4,5,6,7], 7))

#print(binarySearch([1,2,3,4,0,81,8,5],5))