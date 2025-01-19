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


'''
2025/01/19 daily challenge

breadth first search + min heap approach

learnt from official editorial:
https://leetcode.com/problems/trapping-rain-water-ii/editorial/
'''


import heapq


class Solution:
    def trapRainWater(self, heightMap: List[List[int]]) -> int:
        m, n = len(heightMap), len(heightMap[0])
        flags = [[0] * n for _ in range(m)]  # 0b1=visited, 0b10=boundary

        h = []  # (height, i, j)

        # add initial boundary
        for j in range(0, n):
            flags[0][j] = 0b10
            heapq.heappush(h, (heightMap[0][j], 0, j))
            flags[-1][j] = 0b10
            heapq.heappush(h, (heightMap[-1][j], m-1, j))
        for i in range(1, m-1):
            flags[i][0] = 0b10
            heapq.heappush(h, (heightMap[i][0], i, 0))
            flags[i][-1] = 0b10
            heapq.heappush(h, (heightMap[i][-1], i, n-1))
        
        dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        water = 0
        while h:
            curr_height, i, j = heapq.heappop(h)

            # visit (i, j)
            flags[i][j] = 0b11

            for dx, dy in dirs:
                dx += i
                dy += j
                if 0 <= dx < m and 0 <= dy < n:
                    if flags[dx][dy]:
                        continue
                    # queue it (add to the boundary)
                    flags[dx][dy] = 0b10
                    adj_height = heightMap[dx][dy]
                    if adj_height < curr_height:
                        water += curr_height - adj_height
                        # overwrite it to trap more water
                        heightMap[dx][dy] = adj_height = curr_height
                    heapq.heappush(h, (adj_height, dx, dy))

        return water

