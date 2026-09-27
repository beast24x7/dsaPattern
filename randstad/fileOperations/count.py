count = 0

with open("resources/input.txt","r") as fp:
    for line in fp:
        count+=1

    print(count)

count = 0
with open("resources/log.txt","r") as fp:
    for line in fp:
        if "ERROR" in line:
            count+=1
    print(count)

dict = {}
with open("resources/log.txt","r") as fp:
    for i in fp:
        if i.startswith("ERROR"):
            error = i.strip()
            dict[error] = dict.get(error,0) + 1 
    print(dict)

