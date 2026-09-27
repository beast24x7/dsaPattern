

def sortDictionary(d):
    return sorted(d.items(),key= lambda x:x[1])

print(sortDictionary({'c':3,'a':1,'b':2}))