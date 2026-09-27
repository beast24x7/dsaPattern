from typing import List

def dedupSorted(arr: List[int]): 
    fixed = 0
    for i in range(1,len(arr)):
        if arr[fixed] != arr[i]:
            fixed +=1
            arr[fixed] = arr[i]
    return arr[:fixed+1]


print(dedupSorted([1,1,1,2,2,3,4]))

def dedupunsorted(arr: List[int]):
    seen = {}
    for i in arr:
        if i not in seen:
            seen[i] = True
    return list(seen.keys())

print(dedupunsorted([1,2,3,9,4,2]))