sorted_array = [-3,-2,-1, 0, 1, 2, 3, 4]

def sortSquares(arr:list):
    res = [0] * len(arr)
    left = 0
    right = write = len(arr)-1

    while left <= right:
        sqRight = arr[right] * arr[right]
        sqLeft = arr[left] * arr[left]

        if sqRight >=sqLeft:
            res[write] = sqRight
            right -=1
            write -=1
        else:
            res[write] = sqLeft
            left +=1
            write -=1
    return res

print(sortSquares(sorted_array))
    
