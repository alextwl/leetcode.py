'''
2023/04/07 daily challenge

depth first search approach

almost the same as problem 1254
'''

class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        ans = 0  # total number of enclaves

        def dfs(i, j):
            '''
            :return: (the number of cells, isEnclave)
            :rtype: Tuple[int, bool]
            '''
            if not(0 <= i < m and 0 <= j < n):
                '''
                reached the boundary, the land is not an enclave.
                '''
                return (0, False)
            
            if grid[i][j] == 0:
                return (0, True)
            
            # visit it
            grid[i][j] = 0

            # traverse deeper
            cells = 1
            isEnclave = True
            for x, y in [(1, 0), (-1, 0), (0, -1), (0, 1)]:
                a, b = dfs(i+x, j+y)
                cells += a
                isEnclave &= b

            return (cells, isEnclave)
        
        for i in range(m):
            for j in range(n):
                a, b = dfs(i, j)
                if b:
                    ans += a
        
        return ans

