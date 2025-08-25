'''
2025/08/25 daily challenge

iteration approach

iterate matrix diagonally and do reversion.
'''


class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        m, n = len(mat), len(mat[0])
        ans = []
        rev = 1

        # iterate from top boundary
        for j in range(n):
            arr = []
            for i in range(0, min(m, n, j + 1)):
                arr.append(mat[i][j-i])
            if rev:
                arr.reverse()
            ans.extend(arr)
            rev ^= 1
        
        # iterate from right boundary
        for i in range(1, m):
            arr = []
            for j in range(n - 1, -1, -1):
                x = i+(n - j - 1)
                if x >= m:
                    break
                arr.append(mat[x][j])
            if rev:
                arr.reverse()
            ans.extend(arr)
            rev ^= 1

        return ans

