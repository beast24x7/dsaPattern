

def dedup(arr:list):
    fixed = 0
    for i in range(1,len(arr)):
        if arr[fixed] != arr[i]:
            fixed +=1
            arr[fixed] = arr[i]
    return(arr[:fixed+1])


print(dedup([1,1,1,2,3,4,4,5]))