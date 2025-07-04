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


'''
super clever math approach

learnt from official editorial 2:
https://leetcode.com/problems/find-the-k-th-character-in-string-game-ii/editorial/#approach-2-mathematics
'''


class Solution:
    def kthCharacter(self, k: int, operations: List[int]) -> str:
        ans = 0
        # reacking k-th char is equivalent to moving forward k-1 chars.
        k -= 1
        for i in range(k.bit_length() - 1, -1, -1):
            if (k >> i) & 1:
                # shift forward by 2**(t-1) chars, check (t-1)-th bit in (k-1) binary form, and apply (t-1)-th op
                ans += operations[i]
        return chr(ord('a') + (ans % 26))

