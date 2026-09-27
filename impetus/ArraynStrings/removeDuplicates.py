def removeDuplicates(arr:list):
    seen = set()
    result = []
    for i in arr:
        if i not in seen:
            seen.add(i)
            result.append(i)
    return result



print(removeDuplicates([1,1,1,2,3,4,5,5,5,6]))


def removeDuplicates1(arr:list):
    fixed = 0
    for j in range(1,len(arr)):
        if arr[fixed] != arr[j]:
            fixed += 1
            arr[fixed] = arr[j]
    return arr[:fixed+1]


print(removeDuplicates1([1,1,1,2,3,4,5,5,5,6]))


