

with open("resources/input.txt","r") as f:
    for line in f:
        print(line)


"""
Interview Follow-up

Why not use:

f.readlines()

Answer:

readlines() loads entire file into memory.

Iterating line-by-line is memory efficient.

Complexity:

Memory: O(1)
"""