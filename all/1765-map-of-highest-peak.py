'''
2025/01/22 daily challenge

level order traversal approach
'''


import collections


class Solution:
    def highestPeak(self, isWater: List[List[int]]) -> List[List[int]]:
        m, n = len(isWater), len(isWater[0])
        mat = [[-1] * n for _ in range(m)]

        # level order BFS
        q = collections.deque()
        for i, row in enumerate(isWater):
            for j, flag in enumerate(row):
                if flag:
                    q.append((i, j))

        height = 0
        while q:
            for _ in range(len(q)):
                i, j = q.popleft()
                if mat[i][j] != -1:
                    continue
                mat[i][j] = height
                for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                    dx += i
                    dy += j
                    if 0 <= dx < m and 0 <= dy < n:
                        q.append((dx, dy))
            height += 1
        return mat

