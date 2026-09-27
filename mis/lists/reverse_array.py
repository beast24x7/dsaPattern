from typing import List
def reverseInPlace(arr:List[int]) -> List[int]:
    i,j = 0, len(arr)-1
    while i<j:
        arr[i],arr[j]=arr[j],arr[i]

        i+=1
        j-=1
    return arr

def reverseArray(arr: List[int]) -> List[int]:
    return arr[::-1]

print(reverseInPlace([1,2,3,4,5,6]))
print(reverseArray([1,2,3,4,5,6]))

