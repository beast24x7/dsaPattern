from typing import List,Set
class RemoveDuplicate:
    def setOperation(arr: List[int]) -> tuple[List[int],Set[int]]:
        seen = set()
        nums = []
        for i in arr:
            if i not in seen:
                seen.add(i)
                nums.append(i)
        return(nums, seen)
    
    def inplaceSlicing(arr: List[int]) -> List[int]:
        if not arr:
            return None
        fixed = 0
        for i in range(1,len(arr)):
            if arr[i] != arr[fixed]:
                fixed +=1
                arr[fixed] = arr[i]
        return(arr)

    
print(RemoveDuplicate.setOperation([1,1,8,2,3,3,4,5]))

print(RemoveDuplicate.inplaceSlicing([1,1,2,2,3,4,4]))