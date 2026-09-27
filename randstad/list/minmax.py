def minMax(arr:list):
    min = arr[0]
    max = arr[0]

    for i in arr:
        if i < min:
            min = i
        elif i > max:
            max = i
    return (min,max)


print(minMax([10,2,3,4,5,6,7,8]))