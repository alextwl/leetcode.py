'''
2026/01/19 daily challenge

prefix sums approach
'''


class Solution:
    def maxSideLength(self, mat: List[List[int]], threshold: int) -> int:
        m, n = len(mat), len(mat[0])
        # build prefix sums for row & column
        hsum = [[0] * (n + 1) for _ in range(m + 1)]
        vsum = [[0] * (n + 1) for _ in range(m + 1)]
        for i, row in enumerate(mat):
            hs = 0
            for j, val in enumerate(row):
                hs += val
                hsum[i+1][j+1] = hs
                vsum[i+1][j+1] = vsum[i][j+1] + val
        # test square sums
        for r in range(min(m, n), 1, -1):
            for i in range(m - r + 1):
                square_sum = sum(hsum[i+j][r-1] for j in range(1, r + 1))
                for j in range(r, n + 1):
                    square_sum = square_sum - (vsum[i+r][j-r] - vsum[i][j-r]) + (vsum[i+r][j] - vsum[i][j])
                    if square_sum <= threshold:
                        return r

        if any(v <= threshold for row in mat for v in row):
            return 1

        return 0


'''
simplified prefix sums + test side length by increasing order.
'''


class Solution:
    def maxSideLength(self, mat: List[List[int]], threshold: int) -> int:
        m, n = len(mat), len(mat[0])
        # build prefix sums for area
        psum = [[0] * (n + 1) for _ in range(m + 1)]

        for i, row in enumerate(mat):
            hs = 0  # current row's prefix sum
            for j, val in enumerate(row):
                hs += val
                # prev row + curr row = (0,0)-to-(i,j)'s area
                psum[i+1][j+1] = psum[i][j+1] + hs

        if any(v <= threshold for row in mat for v in row):
            ans = 1
        else:
            return 0

        # test square sums
        for r in range(2, min(m, n) + 1):
            for i in range(r, m + 1):
                for j in range(r, n + 1):
                    # big square from (0,0) - top rectangle -
                    # left rectangle + top-left rectangle which's removed twice.
                    square_sum = psum[i][j] - psum[i - r][j] - \
                                psum[i][j - r] + psum[i - r][j - r]
                    if square_sum <= threshold:
                        ans = r
                        break
                if ans == r:
                    break
            if ans != r:
                break

        return ans

