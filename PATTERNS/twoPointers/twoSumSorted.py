from typing import List, Tuple
def twoSum(arr:List[int], target: int) -> List[Tuple[int,int]]:
    left, right = 0, len(arr) - 1
    result = []
    while left < right:
        sum = arr[left] + arr[right]
        if sum == target:
            result.append((arr[left],arr[right]))
            left += 1
            right -= 1
        elif sum < target:
            left += 1
        elif sum > target:
            right -= 1
    return result



print(twoSum([1,2,3,4,5,6,7],5))