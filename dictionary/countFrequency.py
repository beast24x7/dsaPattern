nums = [1,2,3,1,2,1,4]
dict = {}
for i in nums:
    dict[i] = dict.get(i,0)+1
print(dict)