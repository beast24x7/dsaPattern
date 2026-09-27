nums=[1,2,2,3,3,4]

from typing import List
def removeDuplicates(nums:List[int]) -> List[int]:
    seen = set()

    for i in nums:
        if i not in seen:
            seen.add(i)
    return list(seen)

print(removeDuplicates(nums))