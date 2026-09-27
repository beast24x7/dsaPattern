from typing import List, Tuple
class MinMax:
    def minMax(nums: List[int]) -> Tuple[int,int] :
        if not nums:
            return (None, None)
        min = nums[0]
        max = nums[0]

        for i in nums:
            if i < min:
                min = i
            elif i > max:
                max = i
        return(min,max)
    
print(MinMax.minMax([1,0,2,-1]))

print(MinMax.minMax([1]))