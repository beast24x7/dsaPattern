
"""
print(RemoveDuplicate.setOperation([1,1,8,2,3,3,4,5]))

print(RemoveDuplicate.inplaceSlicing([1,1,2,2,3,4,4]))
"""


def removeDuplicatesSetOperation(arr:list):
    seen = set()
    for i in arr:
        if i not in seen:
            seen.add(i)
    return list(seen)

print(removeDuplicatesSetOperation([1,1,8,2,3,3,4,5]))


def removeDuplicatesInplace(arr:list):
    fixed = 0
    for i in range(1,len(arr)-1):
        if arr[fixed] != arr[i]:
            fixed += 1
            arr[fixed] = arr[i]
    return arr[:fixed+1]
print(removeDuplicatesInplace([1,1,2,2,3,4,4]))