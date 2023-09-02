#class Solution(object):

nums1 = [1,2,6,9]
nums2 =[3,4,7,11]
def findMedianSortedArrays(nums1, nums2):
    nums1.extend(nums2)
    nums1.sort()
    print(str(nums1))
    half = len(nums1)// 2
    print(str(half))
    if len(nums1) % 2 == 0:
        l = (nums1[half-1] + nums1[half])/2
        
        return l
    else:
        return nums1[half]
    
print(findMedianSortedArrays(nums1, nums2))
    