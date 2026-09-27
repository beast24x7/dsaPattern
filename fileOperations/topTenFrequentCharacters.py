
d = {}

with open("resources/input.txt","r") as fp:
    for line in fp:
        for word in line.lower().split():
            d[word] = d.get(word,0) + 1
    dict_item = d.items()

    s = sorted(dict_item,key= lambda x: x[1],reverse= True)[:10]

    print(dict(s))