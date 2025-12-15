'''
2025/12/15 daily challenge

combinatorics approach
'''


class Solution:
    def getDescentPeriods(self, prices: List[int]) -> int:
        ans = 0
        period_len = 0
        prev = prices[0] + 1
        for v in prices:
            # equivalent to n * (n - 1) // 2 for total combinations
            # of the longest smooth descent period of current day.
            ans += period_len

            if prev - 1 == v:
                period_len += 1
            else:
                period_len = 1

            prev = v

        ans += period_len  # periods with the last day
        return ans

