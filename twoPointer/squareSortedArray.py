from typing import List

def sortedSquares( nums: List[int]):
    positive = []
    negative = []
    for i in range(0, len(nums)):
        if nums[i] >= 0:
            positive.append(nums[i])
        else :
            negative.append(nums[i])
    squaredPositive = [x * x for x in positive]
    squaredNegative = [x * x for x in negative] [::-1]
    print(f"{nums}")
    print(f"{squaredNegative}")
    print(f"{squaredPositive}")

    final = []
    i = j = 0

    while i < len(squaredNegative) and j < len(squaredPositive):
        if squaredNegative[i] <= squaredPositive[j]:
            final.append(squaredNegative[i])
            i += 1
        else:
            final.append(squaredPositive[j])
            j += 1


    while i < len(squaredNegative):
        final.append(squaredNegative[i])
        i +=1

    while j < len(squaredPositive):
        final.append(squaredPositive[j])
        j += 1

    return final




#print(sortedSquares([-3,-2,-1, 0, 1, 2, 3, 4]))


def twoPointerSortedSquares(nums: List[int]) -> List[int]: 
    left = 0
    write = right = len(nums) -1
    result = [0] * len(nums)

    while left <= right:
        sqRight = nums[right] * nums[right]
        sqLeft = nums[left] * nums [left]
        if  sqRight >= sqLeft:
            result[write] = sqRight 
            right -= 1
            write -= 1
        else:
            result[write] = sqLeft
            left +=1 
            write -=1
    return result

print(twoPointerSortedSquares([-3,-2,-1, 0, 1, 2, 3, 4]))



