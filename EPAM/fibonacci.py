def fiboncci(num):
    if num <= 1:
        return num
    else:
        return fiboncci(num-1) + fiboncci(num-2)
    
print(fiboncci(10))


def fibonacci1(num):
    a=0
    b=1

    for i in range(num):
        print(a, end= " ")
        a,b = b+a,a
fibonacci1(5)