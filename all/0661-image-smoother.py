'''
2023/12/19 daily challenge

iteration approach
'''


class Solution:
    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
        m, n = len(img), len(img[0])

        ans = [[0] * n for _ in range(m)]
        
        for i in range(m):
            # init with (i-1, 0), (i, 0), (i+1, 0) cells
            cells = 0
            total = 0
            for x, y in [(i-1, 0), (i, 0), (i+1, 0)]:
                if 0 <= x < m:
                    cells += 1
                    total += img[x][y]

            for j in range(n):
                # remove the left-left-side column
                for x, y in [(i-1, j-2), (i, j-2), (i+1, j-2)]:
                    if 0 <= x < m and 0 <= y < n:
                        cells -= 1
                        total -= img[x][y]

                # and accumulate the right-side column
                for x, y in [(i-1, j+1), (i, j+1), (i+1, j+1)]:
                    if 0 <= x < m and 0 <= y < n:
                        cells += 1
                        total += img[x][y]
                
                ans[i][j] = total // cells

        return ans

