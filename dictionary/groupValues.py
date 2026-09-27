words = [
    "cat",
    "dog",
    "apple",
    "banana"
]

dict = {}

for i in words:
    dict.setdefault(len(i),[]).append(i)

print(dict)
