
dict = {}
with open("resources/input.txt","r") as f:
    for line in f:
        cleaned_line = line.split()
        for i in cleaned_line:
            dict[i] = dict.get(i,0) + 1
#print(dict) 


nums = [1, 1, 1, 2, 2, 2, 3]

d = {}
for i in nums:
    d[i] = d.get(i,0)+1

print(d)



buckets = [[] for _ in range(len(nums)+1)]

print(buckets)

for key,value in d.items():
    buckets[value].append(key)


print(buckets)

result = []
for i in range(len(buckets)-1,-1,-1):
    if buckets[i]:
        result.append()
        if len(result) == 2:
            print(result)





