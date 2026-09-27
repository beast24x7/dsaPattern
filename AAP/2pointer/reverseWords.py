def reverseWords(s:str):
    s = [str(x) for x in s]
    for i in range(len(s)-1,-1,-1):
        print(s[i],end="")


reverseWords("abc")