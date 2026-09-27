s = "datascience"

dict = {}

for i in s:
    dict[i] = dict.get(i,0)+1

print(dict)