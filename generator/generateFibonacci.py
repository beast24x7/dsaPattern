
def fibonacci():
    a = 0
    b = 1

    for i in range(100):
        yield a
        a,b = b, a+b

result = fibonacci()

for _ in range(5):
    print(next(result))


nums = (x for x  in range(10))
print(next(nums))


