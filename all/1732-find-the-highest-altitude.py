'''
2023/06/19 daily challenge
2026/06/19 daily challenge

prefix sum approach
'''


class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        highest = prefix_sum = 0
        for g in gain:
            prefix_sum += g
            highest = max(highest, prefix_sum)
        return highest


'''
oneliner ver
'''


import itertools


class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        return max(0, max(itertools.accumulate(gain)))

