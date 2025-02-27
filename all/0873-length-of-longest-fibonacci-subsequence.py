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

