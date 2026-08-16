'''
2026/08/16 daily challenge

counter + logic approach

learnt from official editorial:
https://leetcode.com/problems/stone-game-ix/editorial/#approach-construction
'''


class Solution:
    def stoneGameIX(self, stones: List[int]) -> bool:
        counts = [0, 0, 0]  # counts[remainder of stone / 3]
        for v in stones:
            counts[v % 3] += 1
        # if removing remainder 1 or 2 of stone couldn't win,
        # remove a remainder 0 to switch turn.
        # (because removing a remainder-0 stone does not affect the remainder
        #  of the sum of all removed values.)
        if counts[0] & 1 == 0:
            # assume both players play optimally, he/she loses if
            # insufficient types of stones to prevent from the sum being divisible.
            return counts[1] and counts[2]
        # Alice plays first, and the possible sequences will be:
        #     abababababa...
        #     ----------
        # (1) 11212121212... and Bob can only remove remainder 1 stones,
        # after Alice removed all remainder 2 stones, Bob loses.
        # (2) 22121212121... and Bob can only remove remainder 2 stones,
        # after Alice removed all remainder 1 stones, Bob loses.
        #
        # Alice can win if the diff between remainder 1 & 2 are >= 2 stones,
        # and Bob will lose after his first turn.
        return abs(counts[1] - counts[2]) > 2

