elem = [1, 1, 1, 2, 2, 3]
def findTopkElements(nums,k):
    d = {}
    for i in nums:
        d[i] = d.get(i,0) + 1
    
    l = sorted(d.items(),key=lambda x:x[1],reverse=True)
    res = []
    for i in range(k):
        res.append(l[i])
    return res



print(findTopkElements([1,1,1,2,2,3],2))