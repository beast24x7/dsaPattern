words=['cat','dog','apple']


def groupByLenth(words):
    d = {}
    for i in words:
        d.setdefault(len(i),[]).append(i)
    return d


print(groupByLenth(words))