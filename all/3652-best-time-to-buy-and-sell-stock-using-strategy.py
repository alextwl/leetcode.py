'''
2025/12/18 daily challenge

prefix sum approach

learnt from official editorial:
https://leetcode.com/problems/best-time-to-buy-and-sell-stock-using-strategy/editorial/#approach-prefix-sum
'''


class Solution:
    def maxProfit(self, prices: List[int], strategy: List[int], k: int) -> int:
        n = len(prices)

        # build prefix sums for prices & strategy
        pfx_price = [0]
        pfx_strategy = [0]
        for p, s in zip(prices, strategy):
            pfx_price.append(pfx_price[-1] + p)
            pfx_strategy.append(pfx_strategy[-1] + p * s)

        ans = pfx_strategy[-1]  # base: unmodified profits
        for i in range(k - 1, n):
            # unmodified left side [0, i-k]
            left = pfx_strategy[i - k + 1]
            # modified k-length window [i-k+1, i]
            # only calculate last k/2 elements [i - k//2 + 1, i]
            # because first k/2 sum is 0. (modified to hold, no profit)
            modded = pfx_price[i + 1] - pfx_price[i - k // 2 + 1]
            # unmodified right side [i+1, n-1]
            right = pfx_strategy[-1] - pfx_strategy[i + 1]
            ans = max(ans, left + modded + right)

        return ans

