arr = [1,2,3]
arr1 = [3,4,5,6]


def mergeSorted(arr:list, arr1:list):
    i = 0
    j = 0
    l = []
    while i < len(arr) and j < len(arr1):
        if arr[i] <= arr1[j]:
            l.append(arr[i])
            i+=1
        else:
            l.append(arr1[j])
            j+=1
    while i < len(arr):
        l.append(arr[i])
        i+=1
    while j < len(arr1):
        l.append(arr1[j])
        j+=1
    return l


print(mergeSorted(arr,arr1))
