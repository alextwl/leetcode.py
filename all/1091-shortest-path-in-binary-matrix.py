'''
2023/06/01 daily challenge

breadth first search approach
'''

import collections


class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        n = len(grid)
        dp = [[float('inf')] * n for _ in range(n)]
        q = collections.deque([(0, 0, 1)])  # [(x, y, minimal depth)]

        directions = [(1, 0), (-1, 0), (0, -1), (0, 1),
                      (-1, -1), (1, 1), (-1, 1), (1, -1)]

        while(q):
            x, y, depth = q.popleft()

            if not(0 <= x < n and 0 <= y < n) or \
                    grid[x][y] != 0 or dp[x][y] <= depth:
                continue
            
            dp[x][y] = depth
            if (x, y) == (n-1, n-1):
                # end reached.
                continue

            # queue next directions
            depth += 1

            for i, j in directions:
                q.append((x+i, y+j, depth))

        return dp[-1][-1] if dp[-1][-1] != float('inf') else -1

