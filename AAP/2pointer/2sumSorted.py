

def twoSum(arr:list,target:int):
    i,j = 0,len(arr)-1
    l = []
    while i < j:
        s = arr[i] + arr[j]
        if s == target:
            l.append((arr[i],arr[j]))
            i+=1
            j-=1
        elif s < target:
            i+=1
        elif s > target:
            j-=1
    return l


print(twoSum([1,2,3,4,5,6,7],5))