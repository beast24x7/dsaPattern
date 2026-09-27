arr = [1,2,3]
arr1 = [3,4,5,6]


def merge2sortedArray(arr:list, arr1:list):
    res = []
    i,j = 0,0
    while i < len(arr) and j < len(arr1):
        if arr[i] <= arr1[j]:
            res.append(arr[i])
            i+=1
        else: 
            res.append(arr1[j])
            j+=1
    while i < len(arr):
        res.append(arr[i])
        i+=1
    while j < len(arr1):
        res.append(arr1[j])
        j+=1
    return res

print(merge2sortedArray(arr,arr1))
