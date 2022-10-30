'''
2022/10/30 daily challenge

BFS approach

learnt from
https://leetcode.com/problems/shortest-path-in-a-grid-with-obstacles-elimination/discuss/451787/Python-O(m*n*k)-BFS-Solution-with-Explanation
'''

import collections


class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        m, n = len(grid), len(grid[0])
        
        if m == 1 and n == 1:
            # start == end
            return 0
        
        # BFS queue of coordinates to be visited
        q = collections.deque([(0, 0, k, 0)])  # (i, j, remaining k obstacles, steps)
        
        '''
        visited coordinates with obstacle removal quotas: (i, j, remaining k obstacles)
        
        some cells with lower k quota may be visited earlier than cells with more quotas,
        this prevents from finding more shorter pathes if such cells weren't visited again with more quotas.
        it's the reason why visited cells are memorized with remaining k quotas.
        '''
        visited = set()
        
        while q:
            x, y, kquota, step = q.popleft()
            
            # go to 4 directions 
            for i, j in [(x-1, y), (x, y-1), (x+1, y), (x, y+1)]:
                # check boundary
                if 0 <= i < m and 0 <= j < n:
                    # visit obstacle
                    if grid[i][j] == 1 and kquota > 0 and (i, j, kquota - 1) not in visited:
                        visited.add((i, j, kquota - 1))
                        q.append((i, j, kquota - 1, step + 1))
                    # visit empty cell
                    if grid[i][j] == 0 and (i, j, kquota) not in visited:
                        if i == m - 1 and j == n - 1:
                            # reached terminal.
                            return step + 1
                        visited.add((i, j, kquota))
                        q.append((i, j, kquota, step + 1))
        
        # the lower right corner is unreachable
        return -1
