from typing import List, Tuple

def twoSum(arr:List[int], target: int)-> List[Tuple[int,int]]:
    seen = {}
    ls = []
    for i,v in enumerate(arr):
        diff = target - v
        if diff in seen:
            ls.append((seen[diff],i))
        seen[v] = i

    return ls
print(twoSum([0,1,2,3,4,5,6],6))



def twoSum1(arr:list,target:int):
    seen = {}
    result = []
    for i,v in enumerate(arr):
        diff = target - v
        if diff in seen:
            result.append((i,seen[diff]))
        seen[v] = i
    return result

print(twoSum1([0,1,2,3,4,5,6],6))