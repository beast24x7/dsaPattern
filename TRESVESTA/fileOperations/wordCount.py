dict = {}
with open("resources/input.txt","r") as fp:
    for line in fp:
        for i in line.strip().split():
            dict[i] = dict.get(i,0) + 1

print(dict)