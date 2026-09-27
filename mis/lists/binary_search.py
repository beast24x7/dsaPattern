
from typing import List
def binary_search(arr:List[int],target: int)-> int:
    low, high = 0, len(arr)-1
    while low <= high:
        mid = (low + high) // 2 
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid +1
        elif arr[mid] > target:
            high = mid - 1 
    return -1

print(binary_search([1,2,3,4,5,7,7],7))



def count_occurrence(arr, target):

    # find first occurrence
    low, high = 0, len(arr) - 1
    first = -1

    while low <= high:
        mid = (low + high) // 2

        if arr[mid] == target:
            first = mid
            high = mid - 1   # go left
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    # if not found
    if first == -1:
        return 0

    # find last occurrence
    low, high = 0, len(arr) - 1
    last = -1

    while low <= high:
        mid = (low + high) // 2

        if arr[mid] == target:
            last = mid
            low = mid + 1   # go right
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    return last - first + 1