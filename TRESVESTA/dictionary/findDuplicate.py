nums = [1,2,3,2,4,1,5,3]
dict = {}
l = []

for i in nums:
    dict[i] = dict.get(i,0) + 1
for key,value in dict.items():
    if value == 2:
        l.append(key)
print(l)