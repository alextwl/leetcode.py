'''
2024/06/06 daily challenge

counter + min heap approach

same as problem 1296 Divide Array in Sets of K Consecutive Numbers
'''

import collections
import heapq


class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize:
            return False

        ctr = collections.Counter(hand)
        h = list(ctr.keys())
        heapq.heapify(h)

        # try to group each card from the smallest
        while h:
            card = h[0]  # 1st card
            for i in range(groupSize):
                next_card = card + i
                if not ctr[next_card]:
                    # insufficient card
                    return False
                ctr[next_card] -= 1
                if ctr[next_card] == 0 and next_card != heapq.heappop(h):
                    # violation: a previous smaller card is not exhausted before the current card
                    return False

        return True

