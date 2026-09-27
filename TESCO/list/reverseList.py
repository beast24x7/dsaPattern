
def reverseList(arr:list):
    i,j = 0,len(arr)-1
    while i < j:
        arr[i],arr[j] = arr[j],arr[i]
        i+=1
        j-=1
    return arr

print(reverseList([1,2,3,4,5]))


def reverseListNewList(arr:list):
    res = []
    for i in range(len(arr)-1,-1,-1):
        res.append(arr[i])
    return res

print(reverseListNewList([1,2,3,4]))