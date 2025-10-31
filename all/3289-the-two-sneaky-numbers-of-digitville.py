'''
2025/10/31 daily challenge

counter approach
'''


import collections


class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        return [k for k, _ in collections.Counter(nums).most_common(2)]

