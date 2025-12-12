'''
greedy method approach

we can move chips to any position with the same parity without cost,
so we select the position where we can move most chips to without any cost,
move other chips to the neighbor of the position,
and then move again to the position with cost=1.
'''


class Solution:
    def minCostToMoveChips(self, position: List[int]) -> int:
        odds = sum(pos & 1 for pos in position)
        evens = len(position) - odds
        return min(odds, evens)

