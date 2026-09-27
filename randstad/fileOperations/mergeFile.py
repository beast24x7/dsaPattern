listOfFiles = ["resources/part1.txt","resources/part2.txt"]


with open("resources/merged.txt","w") as fp:
    for i in listOfFiles:
        with open(i,"r") as f:
            for line in f:
                fp.write(line+"\n")