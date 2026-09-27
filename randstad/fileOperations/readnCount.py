d = {}
with open("resources/input.txt","r") as fp:
    for i in fp:
        words = i.strip().split(" ")
        for j in words:
            d[j.lower()] = d.get(j.lower(),0) + 1

    print(sorted(d.items(),key=lambda x:x[1],reverse=True))