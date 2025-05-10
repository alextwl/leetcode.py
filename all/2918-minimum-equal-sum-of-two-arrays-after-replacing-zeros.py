'''
2025/05/10 daily challenge

math approach

learnt from official editorial:
https://leetcode.com/problems/minimum-equal-sum-of-two-arrays-after-replacing-zeros/editorial/
'''


class Solution:
    def minSum(self, nums1: List[int], nums2: List[int]) -> int:
        zero1 = nums1.count(0)
        zero2 = nums2.count(0)
        # minimize the sum of each array by replacing zeroes with ones.
        sum1 = sum(nums1) + zero1
        sum2 = sum(nums2) + zero2

        if (not zero1 and sum2 > sum1) or (not zero2 and sum1 > sum2):
            # insufficient replacable slot to make two arrays equal
            return -1
        
        # select the larger one. the smaller one can always replace zeroes
        # with larger integers to let two arrays become equal.
        return max(sum1, sum2)

