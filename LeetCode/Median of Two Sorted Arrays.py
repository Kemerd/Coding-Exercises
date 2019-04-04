'''
= D. Everett Hinton =

https://leetcode.com/submissions/detail/219967799/

Runtime: 60 ms, faster than 98.72% of Python3 online submissions for Median of Two Sorted Arrays.
Memory Usage: 13.4 MB, less than 5.11% of Python3 online submissions for Median of Two Sorted Arrays.

Made using Python 3, not Python 2.

'''

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums = sorted(nums1 + nums2)
        size = len(nums)
        if (size % 2) == 0:
            return float(((nums[int(size/2)]+nums[(int(size/2))-1]))/2) 
        else:
            return float(nums[int(((size/2)+0.5)-1)])
