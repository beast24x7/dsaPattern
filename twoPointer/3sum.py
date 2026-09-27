from typing import List
def threeSum(nums: List[int]) -> List[List[int]]:
    i = 0
    result = []
    nums.sort()
    for i in range(len(nums)-2):
        # skipping if duplicates in i
        if i > 0 and nums[i] == nums[i-1]:
            continue
        left = i+1
        right = len(nums) - 1 

        while left < right:
            s = nums[i] + nums[left]+nums[right]

            if s == 0:
                result.append([nums[i], nums[left], nums[right]])
                left +=1
                right -=1
                while left < right and nums[left] == nums[left-1]:
                    left += 1
                while left < right and nums[right] == nums[right + 1]:
                    right -= 1
            elif s < 0:
                left +=1
            else:
                right -=1
    return result

print(threeSum([-4,-1, 2,2, -1, 0]))
