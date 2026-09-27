#[1,1,2,2,3,3]

from typing import List
def twoSumWithDuplicatesAllCombinations(nums: List[int],target: int) -> List[List[int]]:
    i = 0
    j = len(nums) - 1
    result = []
    while i < j:
        s = nums[i] + nums[j]
        if s  == target:
            result.append([nums[i],nums[j]])
            i += 1
            j -= 1
            while i < j and nums[i] == nums[i-1]:
                i += 1 
            while i < j and  nums[j] == nums[j+1]:
                j -= 1
        elif s < target:
            i +=1
        else:
            j -=1
    return result


print(twoSumWithDuplicatesAllCombinations([0,1,1,2,2,3,4],4))