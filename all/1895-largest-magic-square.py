'''
2026/01/18 daily challenge

prefix sum + exhaustive method approach

build prefix sums for rows & columns,
and calculate diagonal sums when enumerating each square.

similar to problem 840, but there's no shortcut to verify properties
just by border sequence since elements in a square are not strictly limited.
'''


class Solution:
    def largestMagicSquare(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        hsum = [[0] * (n + 1) for _ in range(m + 1)]
        vsum = [[0] * (n + 1) for _ in range(m + 1)]

        for i, row in enumerate(grid):
            hs = 0
            for j, v in enumerate(row):
                # horizontal
                hs += v
                hsum[i+1][j+1] = hs
                # vertical
                vsum[i+1][j+1] = vsum[i][j+1] + v
        
        def verify(x, y, k):
            target = hsum[x+1][y+k] - hsum[x+1][y]
            # horizontal check
            for i in range(1, k):
                if hsum[x+1+i][y+k] - hsum[x+1+i][y] != target:
                    return False
            # vertical check
            for i in range(k):
                if vsum[x+k][y+1+i] - vsum[x][y+1+i] != target:
                    return False
            # slash diagonal check
            diag_sum = sum(grid[x+i][y+i] for i in range(k))
            if diag_sum != target:
                return False
            # backslash diagonal check
            diag_sum = sum(grid[x+i][y+k-1-i] for i in range(k))
            if diag_sum != target:
                return False
            return True

        # start from verifying largest edge length
        for k in range(min(m, n), 1, -1):
            for x in range(m - k + 1):
                for y in range(n - k + 1):
                    if verify(x, y, k):
                        return k

        return 1


'''
full prefix sums ver

also build prefix sums for all diagonal lines.
'''


class Solution:
    def largestMagicSquare(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        # build prefix sums
        hsum = [[0] * (n + 1) for _ in range(m + 1)]  # horizontal
        vsum = [[0] * (n + 1) for _ in range(m + 1)]  # vertical
        ssum = [[0] * (n + 2) for _ in range(m + 1)]  # slash diagonal
        bsum = [[0] * (n + 2) for _ in range(m + 1)]  # backslash diagonal

        for i, row in enumerate(grid):
            hs = 0
            for j, v in enumerate(row):
                # horizontal
                hs += v
                hsum[i+1][j+1] = hs
                # vertical
                vsum[i+1][j+1] = vsum[i][j+1] + v
                # slash
                ssum[i+1][j+1] = ssum[i][j+2] + v
                # backslash
                bsum[i+1][j+1] = bsum[i][j] + v

        def verify(x, y, k):
            target = hsum[x+1][y+k] - hsum[x+1][y]
            # horizontal check
            for i in range(1, k):
                if hsum[x+1+i][y+k] - hsum[x+1+i][y] != target:
                    return False
            # vertical check
            for i in range(k):
                if vsum[x+k][y+1+i] - vsum[x][y+1+i] != target:
                    return False
            # slash diagonal check
            if ssum[x+k][y+1] - ssum[x][y+k+1] != target:
                return False
            # backslash diagonal check
            if bsum[x+k][y+k] - bsum[x][y] != target:
                return False
            return True

        # start from verifying largest edge length
        for k in range(min(m, n), 1, -1):
            for x in range(m - k + 1):
                for y in range(n - k + 1):
                    if verify(x, y, k):
                        return k

        return 1

