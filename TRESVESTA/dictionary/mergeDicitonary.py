d1 = {"a":1,"b":2}
d2 = {"b":5,"c":10}
d3 = {"c":11,"d":15}


d1.update(d2)
print(d1)

for key,value in d3.items():
    d1[key] = value
print(d1)