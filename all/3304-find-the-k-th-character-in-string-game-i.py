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


'''
math approach

learnt from official editorial:
https://leetcode.com/problems/find-the-k-th-character-in-string-game-i/editorial/#approach-iteration
'''


class Solution:
    def kthCharacter(self, k: int) -> str:
        ans = 0
        while k != 1:
            # k = 2**t + a
            t = k.bit_length() - 1
            if (1 << t) == k:
                # a = 0, k' = k - 2**(t-1)
                t -= 1
            # k' = k - 2**t = a
            k -= 1 << t
            # since 1 <= k <= 500 < 512 == 2**9,
            # the answer will eventually smaller than a+9,
            # no need to worry about exceeding z.
            ans += 1
        return chr(ord('a') + ans)

