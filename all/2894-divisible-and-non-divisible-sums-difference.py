'''
2025/05/27 daily challenge

math approach
'''


class Solution:
    def differenceOfSums(self, n: int, m: int) -> int:
        return (n * (n+1) // 2) - sum(range(m, n+1, m)) * 2

