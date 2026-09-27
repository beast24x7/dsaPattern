dct = {}
with open("resources/input.txt","r") as fp:
    for line in fp:
        for word in line.strip().split(" "):
            dct[word] = dct.get(word,0) + 1

print(dct)


print(sorted(dct.items(),key=lambda x:x[1],reverse=True)[:10])