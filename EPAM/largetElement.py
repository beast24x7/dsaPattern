

def largestElement(nums):
    largest = float('-inf')
    for i in nums:
        if i > largest:
            largest = i
    return largest


print(largestElement([1,4,2,8,0]))
