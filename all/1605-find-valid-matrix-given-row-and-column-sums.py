'''
2024/07/20 daily challenge

greedy method approach

since it's guaranteed there's at least one matrix ans
so we can simulate row/column summations again
and fill any numbers as large as possible.
'''


class Solution:
    def restoreMatrix(self, rowSum: List[int], colSum: List[int]) -> List[List[int]]:
        curr_row_sum = [0] * len(rowSum)
        curr_col_sum = [0] * len(colSum)

        ans = []

        for i, i_row_sum in enumerate(rowSum):
            row = []
            for j, j_col_sum in enumerate(colSum):
                # prevent from exceeding row sum or column sum
                k = min(i_row_sum - curr_row_sum[i],
                        j_col_sum - curr_col_sum[j])
                row.append(k)
                curr_row_sum[i] += k
                curr_col_sum[j] += k
            ans.append(row)

        return ans


'''
time/space optimized ver

learnt from official solution 3:
https://leetcode.com/problems/find-valid-matrix-given-row-and-column-sums/solution/
'''


class Solution:
    def restoreMatrix(self, rowSum: List[int], colSum: List[int]) -> List[List[int]]:
        m, n = len(rowSum), len(colSum)

        ans = [[0] * n for _ in range(m)]

        i = j = 0
        while (i < m and j < n):
            # if rowSum[i] was selected as k,
            # the remaining slots of the row are zeroed
            # because the row sum is exhausted,
            # so no need to iterate the same row and
            # we can just go to next row.
            #
            # this is the same for column sum selected case.
            k = min(rowSum[i], colSum[j])
            ans[i][j] = k
            rowSum[i] -= k
            colSum[j] -= k

            if rowSum[i] == 0:
                i += 1
            else:
                j += 1

        return ans

