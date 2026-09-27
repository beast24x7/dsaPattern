from typing import List

def missingNumbers(nums: List[int]) -> List[int] :
    return [x for x in range(min(nums),max(nums)) if x not in nums]

print(missingNumbers([1,2,3,9]))

print(isinstance([1,2,3,4]))