'''
2025/04/23 daily challenge

counter approach
'''


import collections


class Solution:
    def countLargestGroup(self, n: int) -> int:
        ctr = collections.Counter()

        for s in map(str, range(1, n+1)):
            ctr[sum(map(int, s))] += 1

        largest_size = 0
        total_groups = 0
        for _, size in ctr.most_common():
            if size < largest_size:
                break
            largest_size = size
            total_groups += 1

        return total_groups

