chunk = 1024

with open("resources/input.txt","r") as fp:
    chunk1 = fp.read(chunk)
    while True:
        if not chunk1:
            break
        print(chunk1)