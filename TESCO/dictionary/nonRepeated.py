nums = [1,2,2,3,1,1,4]

dict = {}


for i in nums:
    dict[i] = dict.get(i,0) + 1

for key,value in dict.items():
    if value == 1:
        print(key,value)
        break