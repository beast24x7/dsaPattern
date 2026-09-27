nums = [1,[2,3],[4,[5,6]]]

def flattenList(nums):
    l = []
    for i in nums:
        if isinstance(i,list):
            l.extend(flattenList(i))
        else:
            l.append(i)
    return(l)


print(flattenList(nums))