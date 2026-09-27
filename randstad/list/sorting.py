def sort(arr:list):
    length = len(arr)
    for i in range(0, length):
        for j in range(0, length - i - 1):
            if arr[j] > arr[j+1]:
                arr[j],arr[j+1] = arr[j+1],arr[j]
    return arr


print(sort([1,4,2,6,4,0,93,9865]))