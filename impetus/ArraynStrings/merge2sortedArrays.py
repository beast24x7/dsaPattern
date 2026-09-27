
arr = [1,2,3]
arr1 = [3,4,5,6]


def mergeArray(arr:list,arr1:list):
    i = 0
    j = 0
    result = []
    while i < len(arr) and j < len(arr1):
        if arr[i] <= arr1[j]:
            result.append(arr[i])
            i+=1
        else:
            result.append(arr1[j])
            j+=1
    while i < len(arr):
        result.append(arr[i])
        i += 1

    while j < len(arr1):
        result.append(arr1[j])
        j += 1
        
    return result


print(mergeArray(arr,arr1))




