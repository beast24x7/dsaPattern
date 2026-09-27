def minMax(arr:list):
    min = float('inf')
    max = float('-inf')

    for i in arr:
        if i < min:
            min = i
        elif i > max:
            max = i
    return (min,max)



print(minMax([1,0,-1,2]))

def minMax1(arr: list):
    min = arr[0]
    max = arr[0]

    for i in arr:
        if i < min:
            min = i
        elif i> max:
            max = i
    return (min,max)

print(minMax1([1]))