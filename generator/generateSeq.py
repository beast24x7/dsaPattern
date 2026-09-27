
def generateNums():
    nums = []

    for i in range(1000000):
        nums.append(i)
    return nums


#print(generateNums())

def generateNum():
    for i in range(10000000):
        yield i

nums = generateNum()

print(next(nums))
print(next(nums))
    