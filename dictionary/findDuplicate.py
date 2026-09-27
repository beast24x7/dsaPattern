nums = [1,2,3,2,4,1,5]
dict = {}

for i in nums:
    dict[i] = dict.get(i,0)+1
for k,v in dict.items():
    if v == 2:
        print("key:{}".format(k))
