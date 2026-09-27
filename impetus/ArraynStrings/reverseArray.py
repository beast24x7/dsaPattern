def reverseArray(arr: list):
    return arr[::-1]

print(reverseArray([1,2,3,4,5]))


def reverseInPlace(arr: list):
    left, right = 0, len(arr)-1
    while left < right:
        arr[left],arr[right] = arr[right],arr[left]
        left +=1 
        right -=1
    return(arr)

print(reverseInPlace([1,2,3,4,5]))