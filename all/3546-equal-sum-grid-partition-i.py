'''
2026/03/25 daily challenge

enumeration approach

iterate by both row & column.
'''


class Solution:
    def canPartitionGrid(self, grid: List[List[int]]) -> bool:
        m, n = len(grid), len(grid[0])
        # try to see if we could make a horizontal cut
        seen = set()
        total_sum = 0
        for row in grid:
            row_sum = sum(row)
            total_sum += row_sum
            seen.add(total_sum)
        
        if total_sum & 1:
            # odd sum cannot make a cut
            return False
        
        target = total_sum // 2
        if target in seen:
            return True

        # try to see if we could make a vertical cut
        curr_sum = 0
        for j in range(n):
            col_sum = 0
            for i in range(m):
                col_sum += grid[i][j]
            curr_sum += col_sum
            if curr_sum == target:
                return True

        return False

