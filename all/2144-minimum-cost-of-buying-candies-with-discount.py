'''
2026/06/01 daily challenge

sorting approach

buy 2 and get a third candy for free in descending order
'''


class Solution:
    def minimumCost(self, cost: List[int]) -> int:
        cost.sort()
        # we can only get a free candy with cost v0
        # where v0 <= v1 <= v2.
        return sum(cost[::-3]) + sum(cost[-2::-3])

