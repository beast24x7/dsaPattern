nums = [1,2,3,2,4,5,1,6]
def duplicates(nums: list):
    d = {}
    l = []
    for i in nums:
        d[i] = d.get(i,0) + 1
    return ({key:value for key, value in d.items() if value >=2 })

print(duplicates(nums))


def countFrequencies(nums: list):
    d = {}
    for i in nums:
        d[i] = d.get(i,0) + 1
    return(d)

print(countFrequencies(nums))
