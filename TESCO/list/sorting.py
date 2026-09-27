arr = [(1,5),(2,0),(7,8)]

def sortTuple(arr:list):
    for i in range(0,len(arr)):
        for j in range(0, len(arr)-i-1):
            if arr[j][1] > arr[j+1][1]:
                arr[j],arr[j+1] = arr[j+1],arr[j]
    return arr


print(sortTuple(arr))

print(sorted(arr,key=lambda x:x[1],reverse= True))


employees = [
    ["John", 25, 50000],
    ["Alice", 30, 40000],
    ["Bob", 25, 45000]
]



def employeeSorting(arr: list,l:int):
    for i in range(0,len(arr)):
        for j in range(0, len(arr)-i-1):
            if arr[j][l] > arr[j+1][l]:
                arr[j],arr[j+1] = arr[j+1],arr[j]

    return arr

print(employeeSorting(employees,2))