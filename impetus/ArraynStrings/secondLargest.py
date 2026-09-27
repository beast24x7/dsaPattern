def secondLargest(arr:list):
    first = float("-inf")
    second = float("-inf")

    for i in arr:
        if i >= first:
            second = first
            first = i
    
    return second


print(secondLargest([1,2,3,4,5,6,6]))


