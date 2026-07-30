'''
2026/07/30 daily challenge

counter + sorting approach

map the most frequent letter to lowest cost key, and so on.
'''


import collections


class Solution:
    def minimumPushes(self, word: str) -> int:
        ctr = sorted(collections.Counter(word).values(), reverse=True)

        ans = 0
        push_cost = 1
        mapped = 0
        for cnt in ctr:
            ans += push_cost * cnt
            mapped += 1
            if mapped == 8:
                mapped = 0
                push_cost += 1
        return ans

