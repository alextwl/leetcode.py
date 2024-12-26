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


'''
dynamic programming approach (iterative ver)
'''


class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        n = len(nums)
        total = sum(nums)
        if abs(target) > total:
            # impossible to build any valid expression
            return 0
        # dp[i][j] = the count of expressions in nums[0..i]
        # when the current sum j (baseline=sum(nums)) equals to target.
        dp = [[0] * (total * 2 + 1) for _ in range(n)]

        dp[0][total + nums[0]] = 1
        dp[0][total - nums[0]] += 1  # nums[0] might be zero, so use += op here.

        for i in range(1, n):
            # iterate all summation within the range of -total..0..total
            for j in range(-total, total + 1):
                j += total
                if dp[i - 1][j] > 0:
                    # plus sign
                    dp[i][j + nums[i]] += dp[i - 1][j]
                    # minus sign
                    dp[i][j - nums[i]] += dp[i - 1][j]

        return dp[-1][total + target]

