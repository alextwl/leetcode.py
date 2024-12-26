'''
2024/12/26 daily challenge

recursion + cache approach
'''


import functools


class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        n = len(nums)

        @functools.cache
        def dfs(i, curr_sum):
            if i == n:
                return 1 if curr_sum == target else 0

            plus = dfs(i + 1, curr_sum + nums[i])
            minus = dfs(i + 1, curr_sum - nums[i])
            return plus + minus

        return dfs(0, 0)

