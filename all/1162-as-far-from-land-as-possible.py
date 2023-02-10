'''
2023/02/10 daily challenge

breadth first search approach
'''

import collections


class Solution:
    def maxDistance(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        q = collections.deque()  # (x, y, distance)

        '''
        convert the grid:
        all cells -> inf (distance to the nearest land is initialized to infinite value)
        and queue all land with new distance 0.
        '''
        for i in range(m):
            for j in range(n):
                if grid[i][j]:
                    # land
                    q.append((i, j, 0))
                grid[i][j] = float('inf')
        
        if not q or len(q) >= m*n:
            return -1
        
        # BFS
        while(q):
            i, j, d = q.popleft()
            if d >= grid[i][j]:
                # current value of the cell has smaller distance,
                # no need to search further
                continue
            grid[i][j] = d

            '''
            search neighbors

            by the Manhattan distance,
            the distance between the current cell and 4-direction cells is 1.
            '''
            d += 1
            for x, y in [(1, 0), (-1, 0), (0, -1), (0, 1)]:
                x, y = i+x, j+y
                if (0 <= x < m) and (0 <= y < n):
                    q.append((x, y, d))

        ans = 0
        for row in grid:
            ans = max(ans, max(row))

        return ans

