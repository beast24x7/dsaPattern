def minMax(arr:list):
    min = float('inf')
    max = float('-inf')

    for i in arr:
        if i<min:
            min = i
        elif i> max:
            max = i
    return (min,max)

print(minMax([1,2,3,4,5,6]))


def removeDuplicates(arr:list):
    s = set()
    for i in arr:
        if i not in s:
            s.add(i)
    return s
print(removeDuplicates([1,2,3,4,3,2,1]))


def inPlaceRemoveDuplicates(arr:list):
    arr = sorted(arr)
    fixed = 0
    for i in range(1,len(arr)):
        if arr[fixed] != arr[i]:
            fixed +=1
        arr[fixed] = arr[i]
    return arr[:fixed+1]


print(inPlaceRemoveDuplicates([1,2,3,4,2,3,5]))


def reverseList(arr:list):
    l = []
    for i in range(len(arr)-1,-1,-1):
        l.append(arr[i])
    return l

print(reverseList([1,2,3,4,5]))

def reverseinplace(arr:list):
    i,j = 0, len(arr)-1

    while i < j:
        arr[i],arr[j] = arr[j],arr[i]
        i+=1
        j-=1
    return arr
print(reverseinplace([1,2,3,4,5]))

# [1,2,3,4,5,6,7,8] k = 3
# [6,7,8,1,2,3,4,5]

[1,2,3,4,5,6,7,8]
[8,7,6,5,4,3,2,1]
[6,7,8,5,4,3,2,1]
[6,7,8,1,2,3,4,5]


def reverseArrayByK(arr:list,k:int):
    def reveseArray(arr:list,left:int,right:int):
        while(left < right):
            arr[left],arr[right] = arr[right],arr[left]
            left +=1
            right -=1
        return arr
    reveseArray(arr,0,len(arr)-1)
    reveseArray(arr,0,k-1)
    reveseArray(arr,k,len(arr)-1)

    return arr


print(reverseArrayByK([1,2,3,4,5,6,7,8],3))
