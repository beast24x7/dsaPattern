dct = {}


with open("resources/log.txt","r") as fp:
    for i in fp:
        if i.startswith("ERROR"):
            val = i.strip().split(" ")
            key,value = val[0],val[1]
            dct[value] = dct.get(key,0) + 1

print(dct)