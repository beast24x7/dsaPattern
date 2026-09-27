arr = [1,[2,3],[4,[5,6]],7]


def flatten(arr: list):
    res = []
    for i in arr:
        if isinstance(i,list):
            res.extend(flatten(i))
        else:
            res.append(i)
    return res



print(flatten(arr))



