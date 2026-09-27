arr = [-4,-1, 2,2, -1, 0]


def threeSum(arr:list):
    l = []
    arr = sorted(arr)
    for i in range(0,len(arr)-2):
        if i > 0 and arr[i] == arr[i-1]:
            continue
        left = i+1
        right = len(arr)-1

        while left < right:
            s = arr[i] + arr[left] + arr[right]
            if s == 0:
                l.append((arr[i], arr[left], arr[right]))
                left += 1
                right -= 1
            elif s < 0:
                left += 1
            else:
                right -= 1
    return l


print(threeSum(arr))

