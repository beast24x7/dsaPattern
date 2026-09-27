s = "aabbccddef"
dict = {}
for i in s:
    dict[i] = dict.get(i,0)+1

print(dict)

for k,v in dict.items():
    if v == 1:
        print(k,v)
        break