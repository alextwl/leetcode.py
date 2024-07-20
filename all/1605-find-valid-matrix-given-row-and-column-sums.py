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

