'''
2023/11/24 daily challenge

greedy method approach

sort the piles and determine which piles players can get.

Bob: the minimums -> piles[:len(n)//3]
I & Alice -> [..., mine, Alice's, mine, Alice's]
'''

import collections


class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort()
        q = collections.deque(piles)

        ans = 0
        while(q):
            # Alice always gets the maximum pile
            q.pop()
            # I can never get the maximum but the secondary next to Alice's pile.
            ans += q.pop()
            # Bob always gets the minimum pile (so he picks from left.)
            q.popleft()

        return ans

