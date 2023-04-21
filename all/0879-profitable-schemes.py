'''
2023/04/21 daily challenge

dynamic programming approach (knapsack)

learnt from
https://leetcode.com/problems/profitable-schemes/solutions/3439508/python-java-c-simple-solution-easy-to-understand/
'''

class Solution:
    def profitableSchemes(self, n: int, minProfit: int, group: List[int], profit: List[int]) -> int:
        '''
        dp[i][j] = the number of schemes (no matter whether it's profitable)
                   for minimum profit _i_ by size _j_ of group members.
        '''
        dp = [[0] * (n+1) for _ in range(minProfit+1)]
        dp[0][0] = 1  # base case: zero profit with empty group is also a scheme.

        # iterate all pairs of group-profit to be joined
        for g_size, p_interest in zip(group, profit):
            for i in range(minProfit, -1, -1):
                # iterate from (max size - current group's size)
                for j in range(n - g_size, -1, -1):
                    '''
                    add all schemes consisted by i profit & j members.

                    we don't need to count schemes for distinct profits larger than minProfit,
                    we can just add these schemes to dp[minProfit][*] so that we don't need to allocate more dp spaces and summarize it.
                    '''
                    dp[min(minProfit, i + p_interest)][j + g_size] += dp[i][j]

        return sum(dp[minProfit]) % 1_000_000_007

