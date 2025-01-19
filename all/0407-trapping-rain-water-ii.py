'''
2025/01/19 daily challenge

depth first search + level order traversal approach (Time Limit Exceeded)
'''


import collections


class Solution:
    def trapRainWater(self, heightMap: List[List[int]]) -> int:
        m, n = len(heightMap), len(heightMap[0])
        m1, n1 = m - 1, n - 1
        max_height = max(h for row in heightMap for h in row)
        ans = 0

        # the last height of visited cells
        visited = [[0] * n for _ in range(m)]

        dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        def dfs(i, j, h):
            # retval: (trap flag, dimension)
            if visited[i][j] == h or heightMap[i][j] >= h:
                visited[i][j] == h
                return (None, 0)
            if i == 0 or j == 0 or i == m1 or j == n1:
                return (False, 0)
            #if visited[i][j] != h - 1:
            #    return (False, 0)

            visited[i][j] = h
            flag = True
            dimension = 1
            for dx, dy in dirs:
                dx += i
                dy += j
                if not(0 <= dx < m and 0 <= dy < n):
                    continue
                next_flag, next_dim = dfs(dx, dy, h)
                if next_flag is None:
                    continue
                if next_flag is False:
                    flag = False
                else:
                    dimension += next_dim
            return (flag, dimension)

        q = collections.deque([(i, j) for j in range(n) for i in range(m)])
        h = 1
        while q or h <= max_height:
            #print("%d: %s" % (h, str(q)))
            width = len(q)
            for _ in range(width):
                x, y = q.popleft()
                trapped, dim = dfs(x, y, h)
                if trapped is True:
                    ans += dim
                    q.append((x, y))
            # queue newer level
            for x, row in enumerate(heightMap):
                for y, next_h in enumerate(row):
                    if next_h == h:
                        q.append((x, y))
            h += 1

        return ans

