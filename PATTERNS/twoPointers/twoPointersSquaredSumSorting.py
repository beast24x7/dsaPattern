def squaredSumSorting(arr:list):
    result = [0] * len(arr)
    left, right = 0, len(arr)-1

    while left < right:
        sqLeft = arr[left] ** 2
        sqRight = arr[right] ** 2
        if sqLeft < sqRight:
            result

    return result


print(squaredSumSorting([1,2,3,4]))