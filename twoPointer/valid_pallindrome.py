
"""
def is_palindrome(s):
    left, right = 0, len(s) - 1
  
    while(left < right):
        while left < right and not s[left].isalnum():
            #print(f"is not a alphanumeric and index {left} value: {s[left]}")
            left = left + 1
        while left < right and not s[right].isalnum():
            #print(f"is not a alpha numeric and index {right} value: {s[right]}")
            right -= 1
        if s[left].lower() != s[right].lower():
            return False
        left +=1
        right -=1 

    return True

"""
from typing import List
def isPallindrome(arr) -> bool :
    left, right = 0, len(arr)-1

    while left < right:
        if arr[left] != arr[right]:
            return False
        left +=1
        right -=1
    return True

print(isPallindrome([1,2,2,1]))