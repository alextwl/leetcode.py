'''
2024/04/20 daily challenge

depth first search approach (recursion ver)
'''


class Solution:
    def findFarmland(self, land: List[List[int]]) -> List[List[int]]:
        m, n = len(land), len(land[0])

        def dfs(x, y, rec_coords=None):
            if not (0 <= x < m and 0 <= y < n):
                return None

            if land[x][y] != 1:
                return None

            if not rec_coords:
                rec_coords = [x, y, x, y]

            land[x][y] = 2  # visited

            rec_coords[0] = min(rec_coords[0], x)  # top-left x
            rec_coords[1] = min(rec_coords[1], y)  # top-left y
            rec_coords[2] = max(rec_coords[2], x)  # bottom-right x
            rec_coords[3] = max(rec_coords[3], y)  # bottom-right y

            for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                dx += x
                dy += y
                dfs(dx, dy, rec_coords)

            return rec_coords

        ans = []

        for i in range(m):
            for j in range(n):
                if (rec := dfs(i, j)) is not None:
                    ans.append(rec)

        return ans

