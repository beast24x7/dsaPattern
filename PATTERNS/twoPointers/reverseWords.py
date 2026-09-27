def reverseWords(s:str):
    res = [str(x) for x in s]
    i,j = 0,len(res)-1
    while i < j:
        res[i],res[j] = res[j],res[i]
        i += 1
        j -=1
    return "".join(map(str,res))

print(reverseWords("hello"))