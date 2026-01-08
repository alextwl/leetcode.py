'''
2023/10/08 daily challenge
2026/01/08 daily challenge

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


'''
bottom-up dynamic programming approach
'''


class Solution:
    def maxDotProduct(self, nums1: List[int], nums2: List[int]) -> int:
        # corner case check
        if nums1[0] > nums2[0]:
            # no need to check (min1, max2) because if
            # the 1st value of nums1 was smaller than nums2's, that means:
            # 1. min(nums1) is explicitly <= max(nums2).
            # 2. if max(nums2) < 0, min1(nums1) also < 0.
            # 3. (min(nums1) > 0 and max(nums2) < 0) will never stand.
            nums1, nums2 = nums2, nums1

        max1, min2 = max(nums1), min(nums2)
        if max1 < 0 and min2 > 0:
            return max1 * min2

        m, n = len(nums1), len(nums2)
        # dp[i][j] = maximum dot product from nums1[:i] & nums2[:j]
        dp = [[-1_000_001] * (n + 1) for _ in range(m + 1)]

        # base case: either one empty subseq makes zero dot product
        for i in range(m):
            dp[i][0] = 0
        for j in range(1, n):
            dp[0][j] = 0

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                product = nums1[i - 1] * nums2[j - 1] + max(0, dp[i - 1][j - 1])
                # 3 choices:
                # (1) pick nums1[i-1] * nums2[j-1] and
                #     inherit from nums1[:i-1] & nums2[j-1] if >= 0
                # (2) inherit from nums1[:i] & nums2[j-1]
                # (3) inherit from nums1[:i-1] & nums2[j]
                dp[i][j] = max(product, dp[i][j-1], dp[i-1][j])

        return dp[m][n]

