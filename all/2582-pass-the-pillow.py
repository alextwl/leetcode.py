'''
2024/07/06 daily challenge

math approach

the pillow will be back to the first person in every (n-1)*2 turns,
use it as the divisor to calculate the final position of the pillow.
'''


class Solution:
    def passThePillow(self, n: int, time: int) -> int:
        mod = time % ((n-1)*2)
        # note the person label is 1-indexed.
        if mod > (n-1):
            return n - (mod - n + 1)
        return mod + 1

