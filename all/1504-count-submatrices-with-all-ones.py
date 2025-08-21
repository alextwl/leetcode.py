'''
2025/08/21 daily challenge

linear search (enumeration) approach

learnt from official editorial 1:
https://leetcode.com/problems/count-submatrices-with-all-ones/editorial/#approach-1-enumeration
'''


class Solution:
    def numSubmat(self, mat: List[List[int]]) -> int:
        m, n = len(mat), len(mat[0])
        # pfx[i][j] = number of consecutive 1's
        #             ending at pfx[i][j] from the left in a row
        pfx = [[0] * n for _ in range(m)]
        ans = 0

        for i, row in enumerate(mat):
            for j, v in enumerate(row):
                if j == 0:
                    # skip first column
                    pfx[i][0] = v
                elif v:
                    # build prefix (width) from the left cell
                    pfx[i][j] = pfx[i][j - 1] + 1
                # extend upper submatrices
                rec = pfx[i][j]
                for k in range(i, -1, -1):
                    rec = min(rec, pfx[k][j])
                    if rec == 0:
                        break
                    ans += rec
        return ans


'''
prefix consecutive 1's + monotonic stack approach
'''


class Solution:
    def numSubmat(self, mat: List[List[int]]) -> int:
        m, n = len(mat), len(mat[0])
        # upper submatrices in monotonic stacks (non-decreasing)
        upper = [list() for _ in range(n)]
        # pfx[i][j] = number of consecutive 1's
        #             ending at pfx[i][j] from the left in a row
        pfx = [0] * n
        ans = 0

        for i, row in enumerate(mat):
            for j, v in enumerate(row):
                if j == 0:
                    # skip first column
                    pfx[0] = v
                else:
                    # build prefix (width) from the left cell
                    pfx[j] = pfx[j - 1] + 1 if v else 0
                # extend upper submatrices
                if pfx[j]:
                    n = len(upper[j])
                    # filter upper submatrices whose width is longer
                    while upper[j] and upper[j][-1] > pfx[j]:
                        upper[j].pop()
                    # push trimmed upper submatrices + the current row
                    upper[j] += [pfx[j]] * (n - len(upper[j]) + 1)
                    ans += sum(upper[j])
                else:
                    upper[j] = []
        return ans

