d = {
    "A":"HR",
    "B":"IT",
    "C":"HR"
}


dict1 = {}

for key,value in d.items():
    dict1.setdefault(value,[]).append(key)

print(dict1)