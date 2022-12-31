'''
2022/12/31 daily challenge

depth first search approach

note the problem requires all unique paths **must** walk over
every non-obstacle square **exactly once**, so do not count paths
with unvisited squares.
'''


class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        ans = 0

        # find the starting square first.
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    start = (i, j)
                    break

        def dfs(i, j):
            nonlocal ans

            if not (0 <= i < m and 0 <= j < n):
                # out of bound
                return
            
            if grid[i][j] == 2:
                # the ending square reached
                # check if all squares visited
                for row in grid:
                    if 0 in row:
                        # unvisited non-obstacle square found
                        # the path is not qualified.
                        return
                ans += 1
                return
            
            # proceed the empty square
            if grid[i][j] == 0:
                # overwrite square value to 3 as visited
                grid[i][j] = 3
                # search 4 directions
                for x, y in [(1, 0), (-1, 0), (0, -1), (0, 1)]:
                    dfs(i+x, j+y)
                # recover the value
                grid[i][j] = 0
        
        # search from neighbors of the starting square
        dfs(start[0]+1, start[1])
        dfs(start[0]-1, start[1])
        dfs(start[0], start[1]-1)
        dfs(start[0], start[1]+1)

        return ans

