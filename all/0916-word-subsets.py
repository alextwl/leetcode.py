'''
2025/01/10 daily challenge

counter approach
'''


import collections


class Solution:
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
        subset = collections.Counter()
        for ctr in map(collections.Counter, words2):
            for c, v in ctr.items():
                if subset[c] < v:
                    subset[c] = v

        ans = []
        for w in words1:
            if collections.Counter(w) >= subset:
                ans.append(w)

        return ans

