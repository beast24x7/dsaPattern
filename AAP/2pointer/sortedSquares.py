sorted_array = [-3,-2,-1, 0, 1, 2, 3, 4]

def sortedSquares(arr:list):
    res = [0] * len(arr)
    write = len(arr)-1
    i,j = 0,len(arr)-1
    while i < j:
        sqi = arr[i] ** 2
        sqj = arr[j] ** 2
        if sqi >= sqj:
            res[write] = sqi
            write -=1
            i += 1 
        else:
            res[write] = sqj
            write -=1
            j = j-1
    return res


print(sortedSquares(sorted_array))
