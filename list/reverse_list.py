from typing import List

class Reverse:
    def newList(nums: List[int])-> List[int]:
        arr = []
        for i in range(len(nums)-1, -1,-1):
            arr.append(nums[i])
        return arr
    
    def inplace(nums: List[int])-> List[int]:
        left, right = 0, len(nums)-1
        while left < right:
            nums[left],nums[right] = nums[right],nums[left]
            left +=1
            right -=1
        return nums
    

print(Reverse.inplace([1,2,3,4,5]))
print(Reverse.newList([1,2,3,4,5]))