# [1,2,3,4,5,6,7,8] k = 3
# [6,7,8,1,2,3,4,5]

#[8,7,6,5,4,3,2,1]
#[6,7,8,5,4,3,2,1]
#[6,7,8,1,2,3,4,5]



def reverseList(arr:list,k):
    def reverse(left,right):
        while left < right:
            arr[left],arr[right] = arr[right],arr[left]
            left +=1
            right -=1
        return arr
    reverse(0,len(arr)-1)
    reverse(0,k-1)
    reverse(k,len(arr)-1)
    return arr

print(reverseList([1,2,3,4,5,6,7,8],3))