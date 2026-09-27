nums = [(1,2),(3,0),(5,6),(7,8)]

def sort(nums):
    for i in range(0,len(nums)-1):
        for j in range(0, len(nums)-i-1):
            if nums[j][1] > nums[j+1][1]:
                nums[j],nums[j+1] = nums[j+1],nums[j]
    return nums

print(sort(nums))

employees = [
    ["John", 25, 50000],
    ["Alice", 30, 40000],
    ["Bob", 25, 45000]
]

print(sorted(employees,key=lambda x:x[2]))