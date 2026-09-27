nums = [1,2,2,3,1,1,4]

dict = {}

for i in nums:
    dict[i] = dict.get(i,0) + 1

print(dict)

m = 0
e = 0

for key,value in dict.items():
    if value > m:
        m = value
        e = key

print(e,m)