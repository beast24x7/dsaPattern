
from typing import List,Tuple
"""
def removeDuplicates(nums: List[int]) -> Tuple[int,List[int]]:
    if not nums:
        return (0,[])
    fixed = 0
    
    for i in range(1, len(nums)):
        if nums[i] != nums[fixed]:
            fixed += 1
            nums[fixed] = nums[i]
            
    return(fixed+1,nums)

print(removeDuplicates([1,1,2,2,3,3,3,4]))
"""


def removeDuplicatesSortedArray(arr:List[int])-> List[int]:
    fixed = 0
    if not arr:
        return []
    for i in range(1,len(arr)):
        if arr[i] != arr[fixed]:
            fixed +=1
            arr[fixed] = arr[i]
    return(arr)
print(removeDuplicatesSortedArray([1,1,2,3,4,4,5]))

