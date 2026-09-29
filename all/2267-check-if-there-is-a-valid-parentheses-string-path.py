'''
2026/09/29 daily challenge

depth first search approach
'''


class Solution:
    def hasValidPath(self, grid: list[list[str]]) -> bool:
        m, n = len(grid), len(grid[0])
        m1, n1 = m - 1, n - 1
        visited = [[set() for _ in range(n)] for _ in range(m)]

        def dfs(depth, x, y):
            if depth < 0:
                return False
            if not (0 <= x < m and 0 <= y < n):
                return False
            if depth in visited[x][y]:
                return False

            visited[x][y].add(depth)
            if grid[x][y] == '(':
                depth += 1
            else:
                depth -= 1
            if depth < 0:
                return False
            if x == m1 and y == n1:
                return depth == 0

            return dfs(depth, x + 1, y) or dfs(depth, x, y + 1)

        return dfs(0, 0, 0)

