'''
2023/08/17 daily challenge

breadth first search approach
'''

import collections


class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        m, n = len(mat), len(mat[0])
        
        q = collections.deque()  # (x, y)
        dp = [[float('inf')] * n for _ in range(m)]
        for i, row in enumerate(mat):
            for j, val in enumerate(row):
                if val == 0:
                    dp[i][j] = 0
                    q.append((i, j))
        
        while(q):
            x, y = q.popleft()
            next_distance = dp[x][y] + 1
            
            for dx, dy in [(1, 0), (-1, 0), (0, -1), (0, 1)]:
                dx += x
                dy += y
                if (0 <= dx < m) and (0 <= dy < n) and dp[dx][dy] > next_distance:
                    dp[dx][dy] = next_distance
                    q.append((dx, dy))

        return dp


'''
in-place modification ver
'''

class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        m, n = len(mat), len(mat[0])
        
        q = collections.deque()  # (x, y)
        for i, row in enumerate(mat):
            for j, val in enumerate(row):
                if val:
                    row[j] = float('inf')
                else:
                    q.append((i, j))
        
        while(q):
            x, y = q.popleft()
            next_distance = mat[x][y] + 1
            
            for dx, dy in [(1, 0), (-1, 0), (0, -1), (0, 1)]:
                dx += x
                dy += y
                if (0 <= dx < m) and (0 <= dy < n) and mat[dx][dy] > next_distance:
                    mat[dx][dy] = next_distance
                    q.append((dx, dy))

        return mat

