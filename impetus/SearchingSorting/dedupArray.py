from typing import List

def dedup(arr:List[int]):
    seen = {}
    for i in arr:
        if i not in seen:
            seen[i] = True
    return list(seen.keys())

print(dedup([1,1,1,2,2,3,4,5]))


def findOccurance(arr: List[int]):
    seen = {}
    for i in arr:
        seen[i] = seen.get(i,0) + 1
    return seen

print(findOccurance([1,2,3,4,5,1,2,3]))