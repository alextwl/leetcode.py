'''
2022/11/30 daily challenge

Counter + set approach

count the occurance of all numbers and convert it to a set.
'''

import collections

class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        counts = collections.Counter(arr)
        return len(counts.keys()) == len(set(counts.values()))

