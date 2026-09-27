text = "python spark python scala spark python"
d = {}

for i in text.split(" "):
    d[i] = d.get(i,0) + 1
print(d)
