'''
2025/08/29 daily challenge

math approach

count all pairs with different parities.

if x = 2, y = 2 in Alice's turn, Alice always loses.
consider cases with more flowers, for all (x + y) == even it eventually will
come to x = 2, y = 2 when each turn is optimal.
to prevent from this, (x + y) must be an odd for Alice's winning.

also see official editorial for the equation:
https://leetcode.com/problems/alice-and-bob-playing-flower-game/editorial/#approach-mathematics
'''


class Solution:
    def flowerGame(self, n: int, m: int) -> int:
        x_even = n >> 1
        x_odd = x_even + (n & 1)
        y_even = m >> 1
        y_odd = y_even + (m & 1)

        return x_even * y_odd + y_even * x_odd

