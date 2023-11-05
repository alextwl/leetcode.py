'''
2023/11/05 daily challenge

queue approach
'''

import collections


class Solution:
    def getWinner(self, arr: List[int], k: int) -> int:
        max_player = max(arr)

        q = collections.deque(arr)
        winner = q.popleft()
        wins = 0

        while (wins < k):
            if winner == max_player:
                # implement the shortcut or the result will be TLE.
                return winner

            player = q.popleft()

            if winner > player:
                q.append(player)
                wins += 1
            else:
                q.append(winner)
                winner = player
                wins = 1

        return winner

