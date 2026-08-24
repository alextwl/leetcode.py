'''
2026/08/24 daily challenge

dynamic programming approach

learnt from official editorial:
https://leetcode.com/problems/stone-game-viii/editorial/#approach-dynamic-programming
'''


class Solution:
    def stoneGameVIII(self, stones: List[int]) -> int:
        n = len(stones)
        curr_sum = 0
        prefix = []
        for v in stones:
            curr_sum += v
            prefix.append(curr_sum)

        dp = [0] * n
        dp[-1] = prefix[-1]
        for i in range(n - 2, 0, -1):
            # current player: max(doesn't choose i, choose i)
            dp[i] = max(dp[i + 1], prefix[i] - dp[i + 1])

        return dp[1]

