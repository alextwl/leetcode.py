'''
2024/08/10 daily challenge

num of island problem + depth first search approach
'''


class Solution:
    def regionsBySlashes(self, grid: List[str]) -> int:
        # expand a cell to a 3x3 submatrix
        mat = []
        for line in grid:
            it = iter(line)
            row0 = []
            row1 = []
            row2 = []
            for c in it:
                if c == ' ':
                    row0.extend([0, 0, 0])
                    row1.extend([0, 0, 0])
                    row2.extend([0, 0, 0])
                elif c == '/':
                    row0.extend([0, 0, 1])
                    row1.extend([0, 1, 0])
                    row2.extend([1, 0, 0])
                else:
                    row0.extend([1, 0, 0])
                    row1.extend([0, 1, 0])
                    row2.extend([0, 0, 1])
            mat.append(row0)
            mat.append(row1)
            mat.append(row2)

        m, n = len(mat), len(mat[0])

        def dfs(x, y):
            if not (0 <= x < m and 0 <= y < n):
                # out of boundary
                return 0
            if mat[x][y]:
                # visited
                return 0

            # visit the cell
            mat[x][y] = 1

            # traverse further
            for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                dfs(x+dx, y+dy)
            return 1

        islands = 0
        for i in range(m):
            for j in range(n):
                if dfs(i, j):
                    islands += 1

        return islands

