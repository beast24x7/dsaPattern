nums = [1,2,2,3,1,1,4]

dict = {}
for i in nums:
    dict[i] = dict.get(i,0) + 1 

l = list(dict.items())
max = 0
for i in range(0,len(l)):
    if l[i][1] > max:
        max = l[i][1]
print(max)
        