"""
Input: arr[] = [1, 1, 2, 2, 2, 2, 3], target = 2
Output: 4
Explanation: target = 2 occurs 4 times in the given array so the output is 4.
"""
from typing import List
def occurance(arr: List[int],target: int) -> int:
    count = 0 
    for i in arr:
        if i == target:
            count+=1
    return count

print(occurance([1,1,2,2,2,2,3],2))

def countOccurence(arr:List[int],target: int) -> int:
    low, high = 0, len(arr)-1
    first = -1

    while low <= high:
        mid = (low + high)//2
        if arr[mid] == target:
            first = mid
            high = mid - 1
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1 
    if first == -1:
        return 0
    
    last = -1
    low, high = 0, len(arr)-1
    
    while low <= high:
        mid = (low + high)//2
        if arr[mid] == target:
            last = mid
            low = mid +1
        elif arr[mid] < target:
            low = mid +1
        else:
            high = mid -1
    if last == -1:
        return 0
        
    return last - first +1 

print(countOccurence([1,1,2,2,2,2,3],3))