#[1,2,3,4,5,6,7,0,2],4


def twoSum(arr:list, target:int):
    seen = {}
    result = []
    for index, value in enumerate(arr):
        diff = target - value
        if diff in seen:
            result.append((seen[diff],index))
        else:
            seen[value] = index
    return result




print(twoSum([1,2,3,4,5,6,7,0,2],4))



def twoSum1(arr:list, target:int):
    seen = {}
    result = []

    for index, value in enumerate(arr):
        diff = target - value

        if diff in seen:
            result.append((seen[diff],index))
        else:
            seen[value] = index
    return result