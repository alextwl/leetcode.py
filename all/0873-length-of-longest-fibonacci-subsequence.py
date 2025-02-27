'''
2025/02/27 daily challenge

brute force approach
'''


class Solution:
    def lenLongestFibSubseq(self, arr: List[int]) -> int:
        n = len(arr)
        nset = set(arr)
        ans = 0

        for i, x0 in enumerate(arr):
            for j in range(i + 1, n):
                x1 = arr[j]
                x2 = x0 + x1
                curr_len = 2

                # keep finding next fibonacci
                while x2 in nset:
                    x1, x2 = x2, x1 + x2
                    curr_len += 1
                    ans = max(ans, curr_len)
        return ans


'''
dynamic programming approach

much slower than brute force because accessing dp space is expensive.
'''


class Solution:
    def lenLongestFibSubseq(self, arr: List[int]) -> int:
        n = len(arr)
        v2i = {v: i for i, v in enumerate(arr)}
        # dp[x][y] = the length of fibonacci subsequence ending with [..., x, y].
        dp = [[0] * n for _ in range(n)]

        ans = 0
        for i2 in range(n):
            x2 = arr[i2]
            for i1 in range(i2):
                x1 = arr[i1]
                x0 = x2 - x1
                i0 = v2i.get(x0, -1)

                if x0 < x1 and i0 >= 0:
                    # x0 found in arr.
                    dp[i1][i2] = dp[i0][i1] + 1
                else:
                    dp[i1][i2] = 2
                ans = max(ans, dp[i1][i2])

        return ans if ans > 2 else 0


'''
two pointers + dynamic programming approach

learnt from official editorial 3:
https://leetcode.com/problems/length-of-longest-fibonacci-subsequence/editorial/#approach-3-optimized-dynamic-programming
'''


class Solution:
    def lenLongestFibSubseq(self, arr: List[int]) -> int:
        n = len(arr)
        v2i = {v: i for i, v in enumerate(arr)}
        # dp[x][y] = the length of fibonacci subsequence ending with [..., x, y].
        dp = [[0] * n for _ in range(n)]

        ans = 0
        for i2 in range(2, n):
            x2 = arr[i2]

            # two pointer to search eligible pairs
            i0 = 0  # left
            i1 = i2 - 1  # right
            while i0 < i1:
                x0x1 = arr[i0] + arr[i1]
                if x0x1 > x2:
                    i1 -= 1
                elif x0x1 < x2:
                    i0 += 1
                else:
                    # eligible pair found
                    dp[i1][i2] = dp[i0][i1] + 1
                    ans = max(ans, dp[i1][i2])
                    # continue shrinking the window
                    # because there may be more eligible pairs
                    i0 += 1
                    i1 -= 1
        return ans + 2 if ans else 0

