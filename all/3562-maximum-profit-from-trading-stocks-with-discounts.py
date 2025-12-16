'''
2025/12/16 daily challenge

3-D dynamic programming + depth first search approach

learnt from official editorial:
https://leetcode.com/problems/maximum-profit-from-trading-stocks-with-discounts/editorial/#approach-tree-dynamic-programming

runtime~=9s
'''


class Solution:
    def maxProfit(self, n: int, present: List[int], future: List[int], hierarchy: List[List[int]], budget: int) -> int:
        m = budget + 1
        g = [[] for _ in range(n)]
        # convert from 1-indexed to 0-indexed
        for boss, employee in hierarchy:
            g[boss - 1].append(employee - 1)

        def dfs(uid):
            full_cost = present[uid]
            half_cost = full_cost // 2

            # dp[purchase_flag][budget]
            dp0 = [0] * m  # parent do not purchase
            dp1 = [0] * m  # parent do purchase

            profit0 = [0] * m  # no discount
            profit1 = [0] * m  # have discount

            u_size = full_cost

            for child in g[uid]:
                child_dp0, child_dp1, child_size = dfs(child)
                u_size += child_size
                # knapsack
                for i in range(budget, -1, -1):
                    for sub_cost in range(min(child_size, i) + 1):
                        if (rem := i - sub_cost) >= 0:
                            profit0[i] = max(profit0[i], profit0[rem] + child_dp0[sub_cost])
                            profit1[i] = max(profit1[i], profit1[rem] + child_dp1[sub_cost])

            # maximize with current node
            for i in range(budget + 1):
                # reset dp0 & dp1 with profit0 base
                dp0[i] = profit0[i]
                dp1[i] = profit0[i]
                if i >= full_cost:
                    # budget i can afford full price of purchase
                    dp0[i] = max(profit0[i],
                                 profit1[i - full_cost] + future[uid] - full_cost)
                if i >= half_cost:
                    # budget i can afford discounted purchase
                    dp1[i] = max(profit0[i],
                                 profit1[i - half_cost] + future[uid] - half_cost)

            return dp0, dp1, u_size

        # traverse starting from CEO. (0)
        # CEO has no parent, only full price applies. [0]
        # profit of full budget is the maximum. [-1]
        return dfs(0)[0][-1]

