'''
2023/10/08 daily challenge

top-down dynamic programming approach
'''

import functools


class Solution:
    def maxDotProduct(self, nums1: List[int], nums2: List[int]) -> int:
        @functools.cache
        def dp(i, j):
            '''
            return the maximum product sum of subsequences
            within the range of nums1[i:] and nums2[j:].
            '''
            if i == len(nums1) or j == len(nums2):
                # one side of empty array makes zero subsequence
                return 0
            # pick (i, j) pair in both sides of subsequences
            product_sum = nums1[i] * nums2[j] + dp(i+1, j+1)
            
            return max(product_sum, dp(i, j+1), dp(i+1, j))
        
        # shortcuts
        if (max1 := max(nums1)) < 0 and (min2 := min(nums2)) > 0:
            return max1 * min2
        if (min1 := min(nums1)) > 0 and (max2 := max(nums2)) < 0:
            return min1 * max2
        
        return dp(0, 0)

