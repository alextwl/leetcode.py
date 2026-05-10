'''
2026/05/10 daily challenge

dynamic programming approach
'''


class Solution:
    def maximumJumps(self, nums: List[int], target: int) -> int:
        n = len(nums)
        dp = [float('-inf')] * n
        dp[0] = 0

        for i in range(1, n):
            for j in range(i):
                if abs(nums[j] - nums[i]) <= target:
                    dp[i] = max(dp[i], dp[j] + 1)

        return -1 if dp[-1] == float('-inf') else dp[-1]

