'''
2024/04/12 daily challenge

counter & set approach
'''

import collections


class Solution:
    def bestHand(self, ranks: List[int], suits: List[str]) -> str:
        if len(set(suits)) == 1:
            return "Flush"

        rank_ctr = collections.Counter(ranks)
        max_freq = rank_ctr.most_common(1)[0][1]

        if max_freq >= 3:
            return "Three of a Kind"
        if max_freq == 2:
            return "Pair"

        return "High Card"

