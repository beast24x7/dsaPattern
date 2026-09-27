def removeDuplicates(arr:list):
    fixed = 0
    if not arr:
        return None
    for i in range(1, len(arr)):
        if arr[i] != arr[fixed]:
            fixed += 1
            arr[fixed] = arr[i]
    return arr


def removeDuplicates1(arr:list):
    seen = set()
    for i in arr:
        if i not in seen:
            seen.add(i)
    return list(seen)



print(removeDuplicates([1,1,1,2,3,4,5,5]))

print(removeDuplicates1([1,1,1,2,3,4,5,5]))