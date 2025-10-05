'''
2022/08/31 daily challenge
2025/10/05 daily challenge

idea: search each cells starting from pacific boundary and atlantic boundary,
and return the union of cells which can be visited from both 2 oceans.
'''

class Solution:
    def __init__(self):
        self.directions = [(-1,0), (0,1), (0,-1), (1,0)]  # north, east, west, south
    
    def dfs(self, heights: List[List[int]], r: int, c: int, visitedSet):
        if (r,c) in visitedSet:
            return
        
        # visit the cell.
        visitedSet.add((r,c))
        
        for diff in self.directions:
            next_r, next_c = r + diff[0], c + diff[1]
            # boundary check and determine if next cells could flow to (r,c)
            if (0 <= next_r < len(heights)) and (0 <= next_c < len(heights[0])) and \
                (heights[r][c] <= heights[next_r][next_c]):
                self.dfs(heights, next_r, next_c, visitedSet)

    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        flow2pacific = set()
        flow2atlantic = set()
        
        m = len(heights)
        n = len(heights[0])
        
        for r in range(0, m):
            self.dfs(heights, r, 0, flow2pacific)  # search from west
            self.dfs(heights, r, n-1, flow2atlantic)  # search from east
        
        for c in range(0, n):
            self.dfs(heights, 0, c, flow2pacific)  # search from north
            self.dfs(heights, m-1, c, flow2atlantic)  # search from south
        
        return list(flow2pacific & flow2atlantic)


'''
breadth first search approach

bfs from shores of two oceans respectively.
'''


class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        m, n = len(heights), len(heights[0])
        def bfs(coords):
            visited = set(coords)
            while coords:
                x, y = coords.pop()
                val = heights[x][y]
                for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                    dx += x
                    dy += y
                    if 0 <= dx < m and 0 <= dy < n and \
                            heights[dx][dy] >= val and \
                            (dx, dy) not in visited:
                        visited.add((dx, dy))
                        coords.append((dx, dy))
            return visited

        pacific = bfs([(0, j) for j in range(n)] + [(i, 0) for i in range(1, m)])
        m1, n1 = m - 1, n - 1
        atlantic = bfs([(m1, j) for j in range(n)] + [(i, n1) for i in range(0, m1)])

        return list(pacific & atlantic)

