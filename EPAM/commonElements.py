

def commonElements(nums1,nums2):
    return list(set(nums1) & set(nums2))


print(commonElements([1,2,3,4,5],[1,3,4,5]))



def unionElements(nums1,nums2):
    return list(set(nums1) | set(nums2))


print(unionElements([1,2,3,4],[5,6,7]))



def differenceElements(nums1,nums2):
    return list(set(nums1) - set(nums2))

print(differenceElements([1,2,3,4,5],[4,5]))