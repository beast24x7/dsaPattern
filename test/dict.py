d = {}
print(d)

d = {"name":"ravi", "age":30}

print(d)
print(d["name"])
print(d.get("name"))

d["city"] = "kanpur"

print(d.get("city"))
del d["city"]

print(d)
print(d.get("names","no daata"))
print(d["name"])

for key,val in d.items():
    print(key,val)
    
"""
for key,values in d.items():
    print(key, values)

#frequency counting

num = [1,2,3,1,3,4,3]
d = {}
for i in num:
    d[i] = d.get(i,0)+1
print(d)
"""



def countFrequency(arr:list):
    dictionary = {}

    for i in arr:
        dictionary[i] = dictionary.get(i,0) + 1
    return dictionary

d = countFrequency([1,1,1,1,2,3,4,4,5])


print(sorted(d.items(),key=lambda x:x[1],reverse=True))

employees = [
    ("Ravi","IT"),
    ("John","HR"),
    ("Sam","IT"),
    ("Mike","Finance")
]

d = {}
for key,value in employees:
    d.setdefault(value,[]).append(key)

print(d)



d = {}
words = [
    "cat",
    "dog",
    "apple",
    "banana"
]

for i in words:
    d.setdefault(len(i),[]).append(i)

print(d)


employees = {
    101: {"name":"Ravi","salary":50000},
    102: {"name":"John","salary":70000},
    103: {"name":"Sam","salary":60000}
}

print(max(employees,key=lambda x:employees[x]["salary"]))


def twoSum(arr:list,target:int):
    seen = {}
    result = []
    for index,number in enumerate(arr):
        diff = target - number
        if diff in seen:
            result.append((seen[diff],index))

        seen[number] = index

    return result

print(twoSum([1,2,3,4,5,0],5))