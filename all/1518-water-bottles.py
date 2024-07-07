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


'''
math approach (oneliner ver)

learnt from
https://leetcode.com/problems/water-bottles/discuss/5431028/python-one-line-math-solution-o-1-beating-100/

if we could obtain a bottle advance of full water, drink it,
and return it along with (numExchange - 1) empty bottles
for an extra bottle of full water,
we can consider it's the bottle we've just borrowed.

     (numBottles - 1)
so, ------------------ is the amount of extra bottles we can obtain.
    (numExchange - 1)

the dividend is (numBottles - 1) because we always need a bottle to reimburse.
'''


class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        return numBottles + (numBottles - 1) // (numExchange - 1)

