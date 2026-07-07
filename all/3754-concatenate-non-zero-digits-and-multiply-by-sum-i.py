'''
2026/07/07 daily challenge

arithmetic conversion + stack approach
'''


class Solution:
    def sumAndMultiply(self, n: int) -> int:
        stack = []
        dsum = 0
        while n:
            n, rem = divmod(n, 10)
            if rem:
                # pick non-zero digit only
                stack.append(rem)
                dsum += rem
        if not stack:
            return 0
        x = stack.pop()
        while stack:
            x = x * 10 + stack.pop()
        return x * dsum

