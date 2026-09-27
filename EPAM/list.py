even = [x for x in range(11) if x % 2 == 0]

print(even)

odd = [x for x in range(11) if x % 2 != 0]

print(odd)

print(["even" if x % 2 == 0 else "odd" for x in range(11)])

matrix = [[1,2],[3,4],[5,6]]

def flattenList(matrix):
    l = []
    for i in matrix:
        if isinstance(i,list):
            l.extend(flattenList(i))
        else:
            l.append(i)
    return l


print(flattenList(matrix))


words = ["Spark", "", "Python", "", "Scala"]

print([x.lower() for x in words if x])


nums = ["10", "20", "30", "40"]

print([int(x) for x in nums])

from typing import List, Tuple

def minMax(arr: List[int]) -> Tuple[int,int]:
    if not arr:
        return(None,None)
    min = arr[0]
    max = arr[0]
    for i in arr:
        if i < min:
            min = i
        elif i > max:
            max = i
    return (min,max)
    
print(minMax([1,5,0,10]))

#[1,1,8,2,3,3,4,5]
def removeDuplicates(arr:List[int]) -> List[int]:
    seen = set()

    for i in arr:
        if i not in seen:
            seen.add(i)
    return seen

print(removeDuplicates([1,1,8,2,3,3,4,5]))


def inPlaceDuplicates(arr:List[int]) -> List[int]:
    fixed = 0
    for i in range(1,len(arr)-1):
        if arr[fixed] != arr[i]:
            fixed +=1
            arr[fixed] = arr[i]
    return arr
print(inPlaceDuplicates([1,1,2,3,3,4]))


def reverseList(arr:List[int]) -> List[int]: 
    left,right = 0,len(arr) - 1

    while left < right:
        arr[left],arr[right] = arr[right],arr[left]
        left +=1
        right -=1
    return arr

print(reverseList([1,2,3,4,5]))


def sorting(arr:List[int]) -> List[int]:
    l = len(arr)
    for i in range(l):
        for j in range(0,l-i-1):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1] = arr[j+1],arr[j]
    return arr

print(sorting([4,2,4,6,1,0]))

def binarySearch(arr:List[int],target:int) -> List[int]:
    left,right = 0, len(arr)-1
    while left <= right:
        mid = (left+right)//2
        if arr[mid] == target:
            return mid
        elif target < arr[mid]:
            right = mid - 1
        elif target > arr[mid]:
            left = mid + 1
    return -1

print(binarySearch([1,2,3,4,5,6,7,8,9],5))