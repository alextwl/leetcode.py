'''
2023/05/10 daily challenge
'''

class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        mat = [[None] * n for _ in range(n)]
        top = left = 0
        bottom = right = n - 1

        it = iter(range(1, n**2 + 1))
        i = 0

        while(top <= bottom and left <= right):
            # -->
            for j in range(left, right+1):
                mat[i][j] = next(it)
            top += 1

            # |
            # v
            for i in range(top, bottom+1):
                mat[i][j] = next(it)
            right -= 1

            # <--
            for j in range(right, left-1, -1):
                mat[i][j] = next(it)
            bottom -= 1

            # ^
            # |
            for i in range(bottom, top-1, -1):
                mat[i][j] = next(it)
            left += 1

        return mat

