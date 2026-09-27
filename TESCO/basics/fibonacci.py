def fibonacci(num:int):
    if num <= 1:
        return num
    else:
        return fibonacci(num-1) + fibonacci(num-2)


for i in range(10):
    print(fibonacci(i))


"""
Time: O(n)
Space: O(n)
"""
