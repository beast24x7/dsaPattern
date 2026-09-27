def binarySearch(arr:list,target:int): 
    low, high = 0, len(arr)-1
    while low <= high:
        mid = (low + high) // 2
        if target == arr[mid]:
            return mid
        elif target < arr[mid]:
            high = mid-1
        elif target > arr[mid]:
            low = mid + 1
    return -1 

print(binarySearch([1,2,3,4,5,6,7,8,9],7))
