def sortArray(arr:list):
    l = len(arr)
    for i in range(l):
        for j in range(l-i-1):
            if arr[j] > arr[j+1]:
                arr[j],arr[j+1] = arr[j+1],arr[j]
    return arr


print(sortArray([1,10,3,2,9,10,5,6]))


print(sorted([1,10,5,2,3,5,2],reverse=True))

employees = [
    ["John", 25, 50000],
    ["Alice", 30, 40000],
    ["Bob", 25, 45000]
]

l = len(employees)
for i in range(l):
    for j in range(l-i-1):
        if employees[j][2] > employees[j+1][2]:
            employees[j][2], employees[j+1][2] = employees[j+1][2],employees[j][2]

print(employees)
