'''
2025/03/28 daily challenge

sorting + min heap approach

proceed queries in sorted order and search the grid by heap gradually.
'''


import heapq


class Solution:
    def maxPoints(self, grid: List[List[int]], queries: List[int]) -> List[int]:
        m, n = len(grid), len(grid[0])
        query_idx = sorted([(v, i) for i, v in enumerate(queries)])
        ans = [0] * len(queries)

        visited = [[False] * n for _ in range(m)]
        points = 0  # a dp space for points earned.
        # start from top-left corner
        h = [(grid[0][0], 0, 0)]  # min-heap: (cell value, x, y)
        visited[0][0] = True

        for q_val, i in query_idx:
            # earn points for cells if its value was smaller than q_val
            while h and h[0][0] < q_val:
                _, x, y = heapq.heappop(h)
                # the current cell's value is strictly smaller than the query,
                # we can earn this point and visit adjacent cells.
                points += 1
                for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                    dx += x
                    dy += y
                    if 0 <= dx < m and 0 <= dy < n and not visited[dx][dy]:
                        heapq.heappush(h, (grid[dx][dy], dx, dy))
                        visited[dx][dy] = True
            ans[i] = points
        return ans


'''
shortest path + binary search approach

(1) change the question to a shortest path problem
(2) run Dijkstra's algorithm and record maximum cell value of the path
(3) maintain an 1D array: arr[points earned] = the threshold (also a maximum cell value of a path)
(4) binary search max point we can earn in each query.

learnt from official editorial 3:
https://leetcode.com/problems/maximum-number-of-points-from-grid-queries/editorial/#approach-3-using-priority-queue-with-binary-search
'''


import heapq


class Solution:
    def maxPoints(self, grid: List[List[int]], queries: List[int]) -> List[int]:
        m, n = len(grid), len(grid[0])

        # Dijkstra's algorithm
        visited = [[False] * n for _ in range(m)]
        visited[0][0] = True
        h = [(grid[0][0], 0, 0)]
        i2t = [0]  # index: points earned (1-indexed), val: threshold
        curr_threshold = 0
        while h:
            cell_val, x, y = heapq.heappop(h)
            curr_threshold = max(curr_threshold, cell_val)
            i2t.append(curr_threshold)

            for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                dx += x
                dy += y
                if 0 <= dx < m and 0 <= dy < n and not visited[dx][dy]:
                    heapq.heappush(h, (grid[dx][dy], dx, dy))
                    visited[dx][dy] = True

        ans = []
        right_bound = len(i2t) - 1
        for q_val in queries:
            l, r = 0, right_bound  # search the points earned
            while l <= r:
                mid = (l + r) // 2
                if i2t[mid] < q_val:  # strictly greater
                    l = mid + 1
                else:
                    r = mid - 1
            ans.append(r)
        return ans

