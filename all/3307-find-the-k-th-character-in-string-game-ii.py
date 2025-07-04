'''
2025/07/04 daily challenge

bitwise math approach

similar to problem 3304
'''


class Solution:
    def kthCharacter(self, k: int, operations: List[int]) -> str:
        ans = 0
        while k != 1:
            t = k.bit_length() - 1
            if (1 << t) == k:
                # a = 0, k = 2**t + a, k' = k - 2**(t - 1)
                t -= 1
            k -= 1 << t
            if operations[t]:
                # in problem 3304 it's always applied.
                ans = (ans + 1) % 26
        return chr(ord('a') + ans)

