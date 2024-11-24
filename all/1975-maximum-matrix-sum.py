'''
2024/11/24 daily challenge

consider the amount of negative numbers in the matrix:

(1) if there were even amount of negatives,
    all numbers can be converted to non-negatives.

(2) if there were odd amount of negatives,
    there's at least **one** odd number in the matrix.

(3) our goal is to maximize the sum,
    if we cannot prevent from having a negative,
    let the minimal absolute number be negative.
'''


class Solution:
    def maxMatrixSum(self, matrix: List[List[int]]) -> int:
        neg_count = 0
        min_abs = float('inf')  # minimum absolute value
        ans = 0

        for row in matrix:
            for v in row:
                if v < 0:
                    v = -v
                    neg_count ^= 1
                ans += v
                min_abs = min(min_abs, v)

        if neg_count:
            # odd amount of negative numbers found.
            # remove positive min_abs from the ans
            # ans remove it again as an negative min_abs.
            ans -= min_abs * 2

        return ans

