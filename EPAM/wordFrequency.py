text = "apple banana apple orange banana apple"
d = {}
def countFrequency(s: str):
    for i in s.split(" "):
        d[i] = d.get(i,0)+1
    return d


print(countFrequency(text))