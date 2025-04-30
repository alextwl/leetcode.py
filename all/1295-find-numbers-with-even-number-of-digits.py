'''
2025/04/30 daily challenge

measure string length approach
'''


class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        return sum(len(s) & 1 == 0 for s in map(str, nums))

