def flatten(arr:list):
    result = []
    for i in arr:
        if isinstance(i,list):
            result.extend(flatten(i))
        else:
            result.append(i)
    return result
print(flatten([[1,2],2,3]))