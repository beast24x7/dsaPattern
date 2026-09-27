nums = [1,2,2,3,1,1,4]
d = {}
for i in nums:
    d[i] = d.get(i,0) + 1
print(d)

print(max(d,key=lambda x:d.get(x)))