def binarySearch(arr:list,target:int):
    left,right = 0, len(arr)-1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid +1
        elif arr[mid] > target:
            right = mid - 1
    return -1


print(binarySearch([10,20,30,40,50,73],73))