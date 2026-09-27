from typing import List

def threeSumClosestTarget(target: int, nums:List[int])-> int:
    i = 0
    diff = float('inf')
    result = 0
    nums.sort()

    for i in range(len(nums)-2):
        if i > 0 and nums[i] == nums[i-1]:
            continue
        left = i +1 
        right = len(nums)-1
        while left < right:
            s = nums[i]+nums[left]+nums[right]
            if abs(s-target) < diff:
                diff = abs(s-target)
                result = s
            elif abs(s -target) == diff:
                res = max(result,s)
            if s < target:
                left += 1
            else:
                right -=1
    return result


print(threeSumClosestTarget(4,[-1, 2, 2, 4]))



        
