from typing import List,Tuple

def minMax(l:list)-> Tuple[int,int] :
    min = 0
    max = 0

    for i in l:
        if i < min:
            min = i
        elif i > max:
            max = i
    return(min,max)

print(minMax([1,2,3,4,-1]))
