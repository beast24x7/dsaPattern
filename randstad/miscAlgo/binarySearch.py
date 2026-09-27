def binarySEarch(arr:list,target:int):
    low, high = 0, len(arr)-1
    while low < high:
        mid = low + high // 2
        if target == arr[mid]:
            return mid
        elif target < arr[mid]:
            high = mid-1
        elif target > arr[mid]:
            low = mid +1
    return -1


print(binarySEarch([1,2,3,4,5,6],3))


def bubbleSort(arr:list):
    l = len(arr)
    for i in range(0,l):
        for j in range(0,l-i-1):
            if arr[j] > arr[j+1]:
                arr[j],arr[j+1] = arr[j+1],arr[j]
    return arr

print(bubbleSort([1,5,2,9,2,0]))