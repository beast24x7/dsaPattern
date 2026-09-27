count = 0
with open("resources/log.txt","r") as fp:
    for line in fp:
        if "ERROR" in line:
            count +=1

print(count)

d = {}

with open("resources/log.txt","r") as fp:
    for line in fp:
        if line.startswith("ERROR"):
            error = line.strip()
            d[error] = d.get(error,0)+1

    print(max(d,key=d.get))
    print(d)
