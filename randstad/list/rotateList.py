

def rotateList(arr:list,k:int):
    def reverse(start:int,end:int):
        while start < end:
            arr[start],arr[end] = arr[end],arr[start]
            start +=1
            end -= 1
    reverse(0,len(arr)-1)
    reverse(0,k-1)
    reverse(k,len(arr)-1)

    return arr

print(rotateList([1,2,3,4,5,6,7,8],3))