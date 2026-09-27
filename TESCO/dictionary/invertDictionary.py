d = {
    "A":"HR",
    "B":"IT",
    "C":"HR"
}

d1 = {}
for key,value in d.items():
    d1.setdefault(value,[]).append(key)
print(d1)