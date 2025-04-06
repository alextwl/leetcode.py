'''
2024/02/09 daily challenge
2025/04/06 daily challenge

dynamic programming approach (recursive ver)

hint: if nums[j] % nums[i] == 0,
then all factors of nums[i] are also the factors of nums[j].
we can extend the subset by appending smaller factors.
'''

import functools


class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        n = len(nums)
        # the order is not important, sort it to make finding pairs easily
        nums.sort()
        
        @functools.cache
        def dp(pos):
            divisor = nums[pos]
            max_sub = list()
            
            # iterate all values (as a dividend) larger than nums[pos] (as a divisor)
            for i in range(pos+1, n):
                if nums[i] % divisor == 0:
                    sub = dp(i)
                    if len(sub) > len(max_sub):
                        max_sub = sub
            
            # note each element can be a valid subset of single element
            # because the question does not mention index i cannot be index j.
            return [divisor] + max_sub
        
        ans = list()
        
        # iterate all subsets within nums[i:]
        for i in range(n):
            sub = dp(i)
            if len(sub) > len(ans):
                ans = sub

        return ans


'''
dynamic programming approach (bottom-up ver)
'''


class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        n = len(nums)
        nums.sort()

        dp = [[v] for v in nums]

        for i in range(n - 2, -1, -1):
            div = nums[i]
            max_subset = []
            for j in range(i + 1, n):
                if len(dp[j]) > len(max_subset) and nums[j] % div == 0:
                    max_subset = dp[j]
            dp[i].extend(max_subset)

        return max(dp, key=len)

