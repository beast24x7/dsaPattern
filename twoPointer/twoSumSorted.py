from typing import List,Tuple
def twoSum(arr:List[int], target:int) -> List[Tuple[int,int]]:
    left, right = 0, len(arr)-1
    list = []
    while left < right:
        if arr[left] + arr[right] < target:
            left +=1
        elif arr[left] + arr[right] > target:
            right -=1
        elif arr[left]+ arr[right] == target:
            list.append((arr[left],arr[right]))
            right -=1
            left +=1
    return list

print(twoSum([1,2,3,4,5],6))



