'''
2025/10/02 daily challenge
'''


class Solution:
    def maxBottlesDrunk(self, numBottles: int, numExchange: int) -> int:
        ans = numBottles

        while numBottles >= numExchange:
            numBottles -= numExchange - 1
            ans += 1  # drink
            numExchange += 1

        return ans

