def removeDuplicate(l:list):
    seen = set()
    for i in l:
        if i not in seen:
            seen.add(i)
    return list(seen)

print(removeDuplicate([1,1,1,3,2,3]))


def inplaceRemoveDuplicates(l:list):
    if not l:
        return None
    fixed = 0 
    for i in range(1,len(l)):
        if l[fixed] != l[i]:
            fixed +=1
            l[fixed] = l[i]
    return l

print(inplaceRemoveDuplicates([1,1,1,2,3,4,5,5]))