'''
2025/07/03 daily challenge

brute force approach
'''


import math


class Solution:
    def kthCharacter(self, k: int) -> str:
        arr = [0]
        for _ in range(math.ceil(math.log2(k))):
            for i in range(len(arr)):
                arr.append((arr[i] + 1) % 26)
        return chr(ord('a') + arr[k - 1])

