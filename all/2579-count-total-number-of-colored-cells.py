'''
2025/03/05 daily challenge

recursion approach
'''


class Solution:
    def coloredCells(self, n: int) -> int:
        if n == 1:
            return 1
        # f(n) = f(n-1) + 4 vertices + 4 side lengthes without vertices
        return self.coloredCells(n - 1) + 4 + (n - 2) * 4


'''
math approach

the difference between f(n) and f(n-1) is 4 * (n - 1).
'''


class Solution:
    def coloredCells(self, n: int) -> int:
        # 4 * (n-1) + ... + 4 * 2 + 4 * 1 + 1 =
        # 4 * (n-1) * n / 2 + 1 =
        return 2 * (n - 1) * n + 1

