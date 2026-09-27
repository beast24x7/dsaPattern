arr = [-4,-1, 2,2, -1, 0]


def threeSum(arr:list):
    result = []
    arr.sort()
    for i in range(0,len(arr)-2):
        if i > 0 and arr[i] == arr[i-1]:
            continue
        left = i+1
        right = len(arr)-1

        while left < right:
            s = arr[i] + arr[left] + arr[right]
            if s == 0:
                result.append((arr[i],arr[left],arr[right]))
                left = left + 1
                right = right - 1  
            elif s < 0:
                left = left + 1
            else:
                right = right - 1
    return result



print(threeSum(arr))
