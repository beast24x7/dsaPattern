def reverseArray(arr: int):
    left, right = 0, len(arr)-1 
    while left <= right:
        arr[left],arr[right] = arr[right],arr[left]
        left += 1
        right -= 1
    return arr

print(reverseArray([1,2,3,4,5,6])) 


print([1,2,3,4,5,6][::-1])