nums = [2,7,11,15]
target = 9

def twoSum(nums:list, target:int):
    d = {}
    l = []
    for i,v in enumerate(nums):
        diff = target - v
        if diff in d:
            l.append((d[diff],i))
        d[v] = i
    return l

print(twoSum([1,2,3,4,5,6,7,0,2],4))


