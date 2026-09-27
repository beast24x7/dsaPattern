a,b = 0,1

for i in range(0,10):
    print(a)
    a,b = b,a+b


def fib(n):
    if n <= 1:
        return n
    return fib(n - 1) + fib(n - 2)

for i in range(5):
    print(fib(i), end=" ")

print("\n")



def fibonacci(n: int):
    if n <=1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)

print(fibonacci(4))


for i in range(4):
    print(fibonacci(i))