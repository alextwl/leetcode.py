'''
2025/08/29 daily challenge

math approach

count all pairs with different parities.

also see official editorial for the theory:
https://leetcode.com/problems/alice-and-bob-playing-flower-game/editorial/#approach-mathematics
'''


class Solution:
    def flowerGame(self, n: int, m: int) -> int:
        x_even = n >> 1
        x_odd = x_even + (n & 1)
        y_even = m >> 1
        y_odd = y_even + (m & 1)

        return x_even * y_odd + y_even * x_odd

