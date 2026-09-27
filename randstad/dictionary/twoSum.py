def twoSum(arr:list,target:int):
    seen = {}
    result = []
    for index, number in enumerate(arr):
        diff = target - number
        if number in seen:
            result.append((seen[diff],index))
        seen[number] = index
    return result



print(twoSum([1,2,3,4,5,6,7,0,2],4))