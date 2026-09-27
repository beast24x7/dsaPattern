text = "apple banana apple mango banana apple"

def wordCount(s: str):
    d = {}
    s = s.split(" ")
    for i in s:
        d[i] = d.get(i,0) + 1
    return d


print(wordCount(text))
