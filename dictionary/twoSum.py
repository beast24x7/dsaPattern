from typing import List, Tuple

def twoSum(nums:List[int], target:int) -> List[Tuple[int,int]]:
    dict = {}
    list = []

    for index, num in enumerate(nums):
        diff = target - num
        if diff in dict:
            list.append((dict[diff],index))
        dict[num] = index
    return list
print(twoSum([1,2,3,4,5,6,7,0,2],4))


