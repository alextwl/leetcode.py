'''
2025/09/06 daily challenge

bitwise counting + sigma approach

learnt from official editorial:
https://leetcode.com/problems/minimum-operations-to-make-array-elements-zero/editorial/#approach-find-patterns--bitwise-operation-statistics

runtime=3786ms, Beats 5.16%
'''


import functools


@functools.cache
def ops_count(v):
    # the number of operations needed to make [1 to v] zero
    count = 0
    i = 1
    base = 1
    while base <= v:
        count += ((i + 1) >> 1) * (min(base * 2 - 1, v) - base + 1)
        i += 1
        base <<= 1
    return count


class Solution:
    def minOperations(self, queries: List[List[int]]) -> int:
        ans = 0
        for l, r in queries:
            # note both sides of [l, r] are inclusive
            ans += (ops_count(r) - ops_count(l - 1) + 1) >> 1
        return ans

