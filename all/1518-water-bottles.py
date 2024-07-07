'''
2024/07/07 daily challenge

simulation approach
'''


class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        drinks = numBottles
        while numBottles >= numExchange:
            new_full, numBottles = divmod(numBottles, numExchange)
            drinks += new_full
            numBottles += new_full
        return drinks

