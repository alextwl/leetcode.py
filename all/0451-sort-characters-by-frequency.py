'''
2022/12/03 daily challenge

pythonic counter approach

count the occurance of case-sensitive alphabets
and then regenerate the string in descending occurance order.
'''

import collections


class Solution:
    def frequencySort(self, s: str) -> str:
        freq = sorted(collections.Counter(s).items(), key=lambda v: -v[1])
        return ''.join(c * k for c, k in freq)


'''
bucket sort approach
Runtime: 30 ms, faster than 99.79% of Python3 online submissions
time=O(n)
'''

import collections


class Solution:
    def frequencySort(self, s: str) -> str:
        counts = collections.Counter(s)
        buckets = collections.defaultdict(list)  # or [list() for _ in range(len(s)+1) in traditional way
        for c, k in counts.items():
            buckets[k].append(c)
        # retrieve chars c from buckets in k's decreasing order
        return ''.join(c * k for k in sorted(buckets, reverse=True) for c in buckets[k])



'''
2024/02/07 daily challenge

counter built-in sort by frequency approach
'''


import collections


class Solution:
    def frequencySort(self, s: str) -> str:
        return "".join(c * t for c, t in collections.Counter(s).most_common())

