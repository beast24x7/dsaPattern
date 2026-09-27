from typing import List, Tuple

def sort(nums:List[Tuple[int,int]],index:int=0)-> List[Tuple[int,int]]:
    l = len(nums)
    for i in range(l):
        for j in range(l-i-1):
            if nums[j][index] > nums[j+1][index]:
                nums[j],nums[j+1]= nums[j+1],nums[j]
    return nums



print(sort([(1,5),(2,0),(7,8)],0))

employees = [
    ["John", 25, 50000],
    ["Alice", 30, 40000],
    ["Bob", 25, 45000]
]

def sortEmployee(arr,index: int=1):
    n = len(arr)
    for i in range(n):
        for j in range(n-i-1):
            if arr[j][index] > arr[j+1][index]:
                arr[j],arr[j+1] = arr[j+1],arr[j]
    return arr


print(sortEmployee([
    ["John", 25, 50000],
    ["Alice", 30, 40000],
    ["Bob", 25, 45000]
],0))