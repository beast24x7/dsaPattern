def occurence(s:str):
    d ={}
    for i in s:
        d[i] = d.get(i,0) + 1
    return d

print(occurence("abcbd"))

def frequency(s:str):
    d = {}
    for i in s:
        d[i] = d.get(i,0)+1

    return d

print(frequency("abcbd"))


employee = {
    "id": 101,
    "name": "Ravi",
    "salary": 50000
}


print(employee["id"])
print(employee.get("name"))
print(employee.get("fame","no value"))