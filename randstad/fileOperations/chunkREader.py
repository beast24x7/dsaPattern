chunkSize = 1024

with open("resources/input.txt", "r") as f:
    while True:
        chunk = f.read(chunkSize)
        print(chunk)
        if not chunk:
            break