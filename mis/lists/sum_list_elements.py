from typing import List
def sum(arr: List[int]) -> int:
    count = 0
    for i in arr:
        count +=i
    return count

print(sum([1,2,3,4,5]))



from functools import reduce

print(reduce(lambda x,y: x+y,[1,2,3,4,5]))