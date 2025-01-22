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


'''
dynamic programming approach

two-pass scan: update from up/left cells & down/right cells.
'''


class Solution:
    def highestPeak(self, isWater: List[List[int]]) -> List[List[int]]:
        m, n = len(isWater), len(isWater[0])
        infheight = m * n  # uninitialized height

        mat = [[infheight] * n for _ in range(m)]

        # fill the water cells
        for i, row in enumerate(isWater):
            for j, flag in enumerate(row):
                if flag:
                    mat[i][j] = 0

        # forward: update heights by up & left neighbors
        for x, row in enumerate(mat):
            for y, curr_height in enumerate(row):
                min_neighbor_height = infheight
                for dx, dy in [(-1, 0), (0, -1)]:
                    dx += x
                    dy += y
                    if 0 <= dx < m and 0 <= dy < n:
                        min_neighbor_height = min(min_neighbor_height, mat[dx][dy])
                row[y] = min(curr_height, min_neighbor_height + 1)

        # backward: update heights by down & right neighbors
        # note: must start from bottom-right corner or it won't work!
        for x in range(m - 1, -1, -1):
            for y in range(n - 1, -1, -1):
                min_neighbor_height = infheight
                for dx, dy in [(1, 0), (0, 1)]:
                    dx += x
                    dy += y
                    if 0 <= dx < m and 0 <= dy < n:
                        min_neighbor_height = min(min_neighbor_height, mat[dx][dy])
                mat[x][y] = min(mat[x][y], min_neighbor_height + 1)

        return mat

