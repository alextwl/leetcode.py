'''
2023/09/16 daily challenge

heap (Dijkstra's algorithm) approach
'''

import heapq


class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        m, n = len(heights), len(heights[0])
        if m == 1 and n == 1:
            # corner case: only 1 cell
            return 0
        
        m_1, n_1 = m-1, n-1
        term_height = heights[-1][-1]
        ans = float('inf')
        '''
        dp[x][y] = the **minimized** value of maximum absolute difference of a path ending at heights[x][y].
        '''
        dp = [[float('inf')] * n for _ in range(m)]
        
        '''
        because the inputs are big, running BFS/DFS is expected to time out.
        so we use a min-heap to always evaluate smallest path's absolute difference
        in order to reduce the calculation. (Dijkstra's algorithm)
        '''
        h = []
        for x, y in [(0, 1), (1, 0)]:
            if 0 <= x < m and 0 <= y < n:
                heapq.heappush(h, (abs(heights[x][y] - heights[0][0]), heights[0][0], x, y))

        while(h):
            '''
            max_diff: path's maximum absolute difference
            prev_height: the height of previous cell
            '''
            max_diff, prev_height, x, y = heapq.heappop(h)

            if x == 0 and y == 0:
                continue
            if x == m_1 and y == n_1:
                diff = abs(term_height - prev_height)
                ans = min(ans, max(max_diff, diff))
                continue
            
            current_height = heights[x][y]
            # the absolute difference from previous cell to current cell
            diff = abs(current_height - prev_height)
            # maximum absolute difference of current path
            max_diff = max(max_diff, diff)
            
            if dp[x][y] <= max_diff:
                '''
                no need to search further because there's another path ending at here
                has a same/smaller maximum absolute difference.
                '''
                continue
            dp[x][y] = max_diff
            
            for dx, dy in [(1, 0), (-1, 0), (0, -1), (0, 1)]:
                dx, dy = dx+x, dy+y
                if (0 <= dx < m and 0 <= dy < n):
                    heapq.heappush(h, (max_diff, current_height, dx, dy))

        return ans

