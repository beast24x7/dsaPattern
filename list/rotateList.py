# [1,2,3,4,5,6,7,8] k = 3
# [6,7,8,1,2,3,4,5]
print(3%9)

from typing import List
class RotateList:
    def reverseKth(nums: List[int],k: int)-> List[int]:
        
        def reverseList(start: int, end: int)-> List[int]:

            while start < end:
                nums[start], nums[end] = nums[end], nums[start]
                start +=1
                end -=1
            return(nums)
    
        reverseList(0,len(nums)-1)
        reverseList(0,k-1)
        reverseList(k,len(nums)-1)

        return nums

print(RotateList.reverseKth([1,2,3,4,5,6,7,8],3))

