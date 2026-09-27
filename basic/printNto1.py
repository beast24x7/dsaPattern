def printn(n:int):
    if n == 1:
        print(1)
    else:
        print(n)
        printn(n-1)


#printn(50)

def printn(n: int):
    if n == 1:
        print(1)
    else:
        print(n)
        printn(n-1)


printn(5)