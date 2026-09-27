"""
Left Rotate by 1
Before:
1 2 3 4 5

After:
2 3 4 5 1

Right Rotate by 1
Before:
1 2 3 4 5

After:
5 1 2 3 4
"""



def reverseArr(arr:list,left:int,right:int):
    while left < right:
        arr[left],arr[right] = arr[right],arr[left]
        left +=1
        right -=1
    return arr

arr = [1,2,3,4,5]
k = 1
reverseArr(arr,0,len(arr)-1)
print(reverseArr(arr,0,len(arr)-1-k))  