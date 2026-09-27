def minMax(arr:list):
    max = float('-inf')
    min = float('inf')

    for i in arr:
        if i < min:
            min = i
        elif i > max:
            max = i
    return(min,max)


print(minMax([1,0,5,2,10,4,19,2,19]))



