nums = [1,2,3,2,4,5,1,6,6,1]


def duplicates(arr:list):
    d = {}
    for i in arr:
        d[i] = d.get(i,0) + 1 
    return {key:value for key, value in d.items() if value > 1}


print(duplicates(nums))

