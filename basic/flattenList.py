arr = [1,[2,3],[4,[5,6]],7]


def flattenList(arr:list):
    l = []
    for i in arr:
        if isinstance(i,list):
            l.extend(flattenList(i))
        else:
            l.append(i)
    return l


print(flattenList(arr))


print(arr)
