from typing import List,Tuple

def twoSum(l:list,target:int) -> List[Tuple[int,int]]:
    result = []
    seen = {}
    for index,num in enumerate(l):
        diff = target - num
        if diff in seen:
            result.append((seen[diff],index))
        seen[num] = index
    return result

print(twoSum([1,2,3,4,5,0],4))