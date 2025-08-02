'''
2025/08/02 daily challenge

greedy method approach

learnt from official editorial:
https://leetcode.com/problems/rearranging-fruits/editorial/#approach-greedy
'''


import collections


class Solution:
    def minCost(self, basket1: List[int], basket2: List[int]) -> int:
        cnt = collections.Counter(basket1)
        min_key = min(cnt.keys())
        # subtract basket1 by basket2
        for v in basket2:
            cnt[v] -= 1
            min_key = min(min_key, v)
        
        merger = []
        for k, c in cnt.items():
            if c & 1:
                # odd sum of frequencies of an element found,
                # impossible to balance both baskets
                return -1
            # if freq1[k] > freq2[k] then ((freq1[k] - freq2[k]) // 2) fruits
            # must be moved from basket1 to basket2, and vice versa.
            merger.extend([k] * (abs(c) // 2))
        
        if not merger:
            return 0
        merger.sort()
        m2 = min_key * 2
        cost = 0
        # pair the smallest vals from the 1st half with the largest from the 2nd half
        for k in merger[:len(merger) // 2]:
            # swap x1 with x2 with a cost of x1,
            # or both exchanged indirectly through min cost fruit.
            # (there're 2 swaps so it's 2 times of min_key costs.)
            cost += min(m2, k)
        return cost

