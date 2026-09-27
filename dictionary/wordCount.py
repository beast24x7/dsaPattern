text = "python spark python scala spark python"
dict = {}
for i in text.split(" "):
    dict[i] = dict.get(i,0)+1
print(dict)