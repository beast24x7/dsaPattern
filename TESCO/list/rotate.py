def rotateList(arr:list,k:int):

    def rotate(first:int,last:int):
        while first < last:
            arr[first],arr[last] = arr[last],arr[first]
            first += 1
            last -= 1
        return arr

    rotate(0,len(arr)-1)
    rotate(0,k-1)
    rotate(k,len(arr)-1)

    return arr

print(rotateList([1,2,3,4,5,6,7,8],3))
