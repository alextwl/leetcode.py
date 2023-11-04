'''
2023/11/04 daily challenge

when 2 ants meet and change their directions,
that's equivalent to 2 ants meet and continue moving
without changing their directions.
'''


class Solution:
    def getLastMoment(self, n: int, left: List[int], right: List[int]) -> int:
        # the longest distance of ant moving to the left bound
        left_max = max(left) if left else 0
        # the longest distance of ant moving to the right bound
        right_max = (n - min(right)) if right else 0
        return max(left_max, right_max)

