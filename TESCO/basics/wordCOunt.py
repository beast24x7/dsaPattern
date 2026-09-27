text = "apple banana apple mango banana apple"


def wordCount(s: str):
    d = {}
    for i in s.split(" "):
        d[i] = d.get(i,0) + 1
    return d

print(wordCount(text))

