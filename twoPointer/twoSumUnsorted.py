from typing import List

"""
[1,2,3,4,5,6]
{5}

def two_sum(nums, target):
    seen = {}

    for i in range(len(nums)):
        num = nums[i]
        need = target - num

        if need in seen:
            return [seen[need], i]

        seen[num] = i

    return []

def two_sum(nums, target):
    seen = {}
    l = []
    for i, num in enumerate(nums):
        needed = target - num

        # check if we already saw the needed number
        if needed in seen:
            l.append((seen[needed], i))

        # store current number
        seen[num] = i
    return l

print(two_sum([1,6,2,3,5,4],6))






def two_sum1(arr,target):
    dict ={}
    list = []

    for i,num in enumerate(arr):
        need = target - num
        if need in dict:
            list.append((num,need))
        dict[num] = i
    return list

print(two_sum1([1,6,2,3,5,4],6))
"""
def twoSum2(arr, target):
    unique = set()
    list = []

    for i in arr:
        find = target - i
        if find in unique:
            list.append((find,i))
        unique.add(i)
    return list
print(twoSum2([1,2,3,4,6,5,4],6))