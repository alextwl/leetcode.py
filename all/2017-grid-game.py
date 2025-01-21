'''
2025/01/21 daily challenge

prefix sum approach

since robot1 tried to minimize robot2's points,
robot2 can only turn down at the 1st column or last column
and collect remaining points in either row0 or row1 optimally.
'''


class Solution:
    def gridGame(self, grid: List[List[int]]) -> int:
        sum_row0 = sum(grid[0])
        sum_row1 = 0

        min_sum = float('inf')
        for a, b in zip(*grid):
            # calculate when robot1 turns down at this position,
            # how many points robot2 can collect.
            sum_row0 -= a
            # robot2 can only collect all remaining points in either row0 or row1 optimally.
            # row0: points after robot1's turning point
            # row1: points before robot1's turning point
            min_sum = min(min_sum, max(sum_row0, sum_row1))
            sum_row1 += b

        return min_sum

