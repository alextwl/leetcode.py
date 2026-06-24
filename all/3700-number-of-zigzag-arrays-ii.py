'''
2026/06/24 daily challenge

dynamic programming + matrix exponentiation approach

learnt from official editorial:
https://leetcode.com/problems/number-of-zigzag-arrays-ii/editorial/#approach-dynamic-programming--matrix-exponentiation

harder version of problem 3699.
'''


MOD = 1_000_000_007


def mul(a, b):
    # matrix multiplication
    n, m = len(a), len(b[0])
    a_width = len(a[0])
    ret = [[0] * m for _ in range(n)]
    for i, a_row in enumerate(a):
        for k in range(a_width):
            r = a_row[k]
            if r == 0:
                continue
            for j in range(m):
                ret[i][j] = (ret[i][j] + r * b[k][j]) % MOD
    return ret


def powMul(base, exp, ret):
    # matrix exponentiation
    while exp > 0:
        if exp & 1:
            ret = mul(ret, base)
        base = mul(base, base)
        exp >>= 1
    return ret


class Solution:
    def zigZagArrays(self, n: int, l: int, r: int) -> int:
        m = r - l + 1
        if n == 1:
            return m

        size = 2 * m
        u = [[0] * size for _ in range(size)]
        for i in range(m):
            for j in range(i):
                u[i][j + m] = 1
            for j in range(i + 1, m):
                u[i + m][j] = 1

        dp = [[1] * size]
        dp = powMul(u, n - 1, dp)
        ans = 0
        for i in range(size):
            ans = (ans + dp[0][i]) % MOD
        
        return ans

