'''
2026/04/26 daily challenge

topological sort approach
'''


import collections


class Solution:
    def containsCycle(self, grid: List[List[str]]) -> bool:
        m, n = len(grid), len(grid[0])
        indegree = [0] * (m * n)
        g = [list() for _ in range(m * n)]

        for i, row in enumerate(grid):
            for j, val in enumerate(row):
                idx0 = i * n + j
                for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                    dx += i
                    dy += j
                    if 0 <= dx < m and 0 <= dy < n and grid[dx][dy] == val:
                        idx1 = dx * n + dy
                        indegree[idx1] += 1
                        g[idx0].append(idx1)

        q = collections.deque([idx for idx, cnt in enumerate(indegree) if cnt == 1])
        while q:
            node = q.popleft()
            if indegree[node] == 0:
                continue
            for adj in g[node]:
                if indegree[adj] == 0:
                    continue
                indegree[adj] -= 1
                if indegree[adj] == 1:
                    q.append(adj)
            indegree[node] = 0

        return any(indegree)

