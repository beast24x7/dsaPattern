s = "datascience"

def countOccurence(s:str)-> dict:
    dict1 = {}
    for i in s.lower():
        dict1[i] = dict1.get(i,0) + 1
    return dict1

print(countOccurence(s))

nums = [1,2,3,1,2,1,4]
def countFrequency(l:list) -> dict:
    dict1 = {}
    for i in l:
        dict1[i] = dict1.get(i,0) + 1
    return dict1

print(countFrequency(nums))