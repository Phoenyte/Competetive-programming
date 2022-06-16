import math
class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        nums=nums1+nums2
        nums.sort()
        if len(nums)%2!=0:
            return nums[math.ceil(len(nums)/2)-1]
        else:
            return (nums[math.ceil(len(nums)/2)]+nums[math.ceil(len(nums)/2)-1])/2