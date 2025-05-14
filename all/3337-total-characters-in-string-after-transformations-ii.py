'''
2025/05/14 daily challenge

matrix multiplication + exponentiating by squaring approach

learnt from official editorial:
https://leetcode.com/problems/total-characters-in-string-after-transformations-ii/editorial/
'''


import collections


class Matrix:
    def __init__(self, copy_from: "Matrix" = None):
        if copy_from:
            self.data = [[v for v in row] for row in copy_from]
        else:
            self.data = [[0] * 26 for _ in range(26)]
    
    def __mul__(self, other: "Matrix") -> "Matrix":
        # matrix multiplication
        ret = Matrix()
        m = ret.data
        for i in range(26):
            for j in range(26):
                for k in range(26):
                    m[i][j] = (m[i][j] + self.data[i][k] * other.data[k][j]) % 1_000_000_007
        return ret


class Solution:
    def lengthAfterTransformations(self, s: str, t: int, nums: List[int]) -> int:
        # build transformation matrix T
        T = Matrix()
        for i, shift in enumerate(nums):
            for j in range(i + 1, i + shift + 1):
                T.data[j % 26][i] = 1

        tt = Matrix()
        for i in range(26):
            tt.data[i][i] = 1
        # matrix exponentiation by squaring
        while t:
            if t & 1:
                tt = tt * T
            T = T * T
            t >>= 1

        ctr = collections.Counter(s)
        f = [ctr[chr(i + ord('a'))] for i in range(26)]

        ans = 0
        for tt_row in tt.data:
            for tt_val, f_val in zip(tt_row, f):
                ans = (ans + tt_val * f_val) % 1_000_000_007

        return ans

