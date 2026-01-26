'''
buy 2 and get a third candy for free in descending order
'''


class Solution:
    def minimumCost(self, cost: List[int]) -> int:
        cost.sort()
        return sum(cost[::-3]) + sum(cost[-2::-3])

