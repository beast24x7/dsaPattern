d = {
    "A":"HR",
    "B":"IT",
    "C":"HR"
}

dict = {}
for key,value in d.items():
    dict.setdefault(value,[]).append(key)

print(dict)
