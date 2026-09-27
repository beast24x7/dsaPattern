def readFile(path):
    with open(path,"r") as fp:
        for line in fp:
            yield line.strip()

result = readFile("resources/input.txt")

for line in result:
    print(line)