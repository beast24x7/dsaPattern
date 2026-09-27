"""
arr = [1, 5, 3, 4, 2]
k = 2

(1,3)
(3,5)
(2,4)
"""

def find_pairs(arr, k):
    seen = set(arr)

    for num in arr:
        if num + k in seen:
            print((num, num + k))


arr = [1, 5, 3, 4, 2]
k = 2

find_pairs(arr, k)



def find_pairs(arr:list, target:int):
    seen = set(arr)
    for i in arr:
        if i+ target in seen:
            print(i,i+target)
