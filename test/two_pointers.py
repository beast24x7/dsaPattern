from typing import List,Tuple
def removeDuplicates(nums: List[int]) -> Tuple[int,List[int]]:
    if not nums:
        return (0,[])
    fixed = 0
    for checker in range(1,len(nums)):
        if nums[checker] != nums[fixed]:
            fixed +=1
            nums[fixed] = nums[checker]
    return(fixed+1,nums)
    

print(removeDuplicates([1,1,2,3,4,4]))
