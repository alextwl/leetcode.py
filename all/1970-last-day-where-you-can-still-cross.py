'''
2023/06/30 daily challenge
2025/12/31 daily challenge

binary search + breadth first search approach
'''

import collections


class Solution:
    def latestDayToCross(self, row: int, col: int, cells: List[List[int]]) -> int:
        # note all the input coordinates are 1-based.
        def isCrossable(day):
            '''
            run BFS on the specific day.
            '''
            mat = [[0] * col for _ in range(row)]
            
            # mark the water on and before the day.
            for r, c in cells[:day]:
                # convert 1-based index to 0-based
                mat[r-1][c-1] = 1
            
            # queue land in the first row.
            q = collections.deque()
            for j, cell in enumerate(mat[0]):
                if cell == 0:
                    q.append((0, j))
                    # visit it in advance
                    mat[0][j] = -1
            
            # BFS
            last_row = row - 1
            while(q):
                i, j = q.popleft()
                if i == last_row:
                    # last row reached
                    return True
                
                # queue 4-direction neighbors
                for x, y in [(1, 0), (-1, 0), (0, -1), (0, 1)]:
                    x += i
                    y += j
                    if 0 <= x < row and 0 <= y < col and mat[x][y] == 0:
                        q.append((x, y))
                        # visit the cells first
                        mat[x][y] = -1
            
            # path to the last row not found.
            return False
        
        # binary search
        left, right = 1, row*col  # day 1 to the max day
        
        while(left < right):
            mid = left + (right - left + 1) // 2
            if isCrossable(mid):
                # mid day is verified crossable, but not mid + 1
                left = mid
            else:
                right = mid - 1

        return left


'''
Union-find approach

proceed cells array reversely with Disjoint set
'''


class Solution:
    def latestDayToCross(self, row: int, col: int, cells: List[List[int]]) -> int:
        # the last two DSUs are dummy sets for top land row & bottom land row.
        parent = [i for i in range(row * col + 2)]
        top_id = row * col
        bottom_id = top_id + 1

        def find(u):
            if parent[u] != u:
                parent[u] = find(parent[u])
            return parent[u]

        def union(u, v):
            u, v = find(u), find(v)
            if u > v:
                parent[v] = u
            elif v > u:
                parent[u] = v

        # build matrix of the latest day
        grid = [[0] * col for _ in range(row)]
        for i, j in cells:
            grid[i-1][j-1] = 1
        for i, r in enumerate(grid):
            for j, val in enumerate(r):
                if not val:
                    idx = i * col + j
                    for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                        dx += i
                        dy += j
                        if 0 <= dx < row and 0 <= dy < col and not grid[dx][dy]:
                            union(idx, dx * col + dy)
        # union top row
        for j, val in enumerate(grid[0]):
            if not val:
                union(top_id, j)
        # union bottom row
        for j, val in enumerate(grid[-1], start=(row - 1) * col):
            if not val:
                union(bottom_id, j)

        # recover from water to land reversely
        for d in range(len(cells) - 1, -1, -1):
            x, y = cells[d]
            x, y = x - 1, y - 1
            idx = x * col + y
            grid[x][y] = 0
            for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                dx += x
                dy += y
                if 0 <= dx < row and 0 <= dy < col and not grid[dx][dy]:
                    union(idx, dx * col + dy)
            # remember to union dummy sets if it's in top or bottom row
            if x == 0:
                union(top_id, idx)
            if x == row - 1:
                union(bottom_id, idx)
            if find(top_id) == find(bottom_id):
                return d
        # undefined behavior
        return -1

