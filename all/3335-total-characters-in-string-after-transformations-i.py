'''
2025/05/13 daily challenge

brute-force method approach
'''


import collections


class Solution:
    def lengthAfterTransformations(self, s: str, t: int) -> int:
        cnt = collections.Counter(s)
        arr = [cnt[chr(ord('a') + i)] for i in range(26)]

        for _ in range(t):
            z = arr[-1]
            for i in range(24, -1, -1):
                arr[i+1] = arr[i]
            arr[0] = z
            arr[1] = (arr[1] + z) % 1_000_000_007

        return sum(arr) % 1_000_000_007

