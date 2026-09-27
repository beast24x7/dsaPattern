from typing import List
def min_max(arr: List[int])-> List[int] :
    min = float('inf')
    max = float('-inf')

    for i in arr:
        if i < min:
            min = i
        elif i > max:
            max = i
    return[min,max]

print(min_max([0,2,5,-1]))


