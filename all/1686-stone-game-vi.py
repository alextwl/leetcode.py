'''
max heap + greedy method approach

pick a stone not only earn its value, but the opponent also lose its value,
so picking a stone optimally means pick the maximum sum of the stone's values greedily.
'''

import heapq


class Solution:
    def stoneGameVI(self, aliceValues: List[int], bobValues: List[int]) -> int:
        h = []  # max heap: (-(alice+bob), -a, -b)
        
        for a, b in zip(aliceValues, bobValues):
            heapq.heappush(h, (-a-b, -a, -b))
        
        alice_points = 0
        bob_points = 0
        
        while(h):
            # alice's turn
            _, na, _ = heapq.heappop(h)
            alice_points -= na

            if not h: break
            # bob's turn
            _, _, nb = heapq.heappop(h)
            bob_points -= nb
        
        if alice_points > bob_points:
            return 1
        if bob_points > alice_points:
            return -1
        # draw
        return 0

