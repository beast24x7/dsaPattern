chunk_size = 1024

with open("resources/input.txt", "r") as f:

    while True:

        chunk = f.read(chunk_size)

        if not chunk:
            break

        print(chunk)

chunk_size = 1024

with open("resources/input.txt","r") as fp:
    while True:
        chunk = fp.read(chunk_size)
        if not chunk:
            break
        print(chunk)