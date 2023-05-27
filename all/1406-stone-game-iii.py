'''
2023/05/27 daily challenge

dynamic programming approach (space=O(1) ver)

learnt from
https://leetcode.com/problems/stone-game-iii/solutions/3566303/python-java-c-simple-solution-easy-to-understand/
'''

class Solution:
    def stoneGameIII(self, stoneValue: List[int]) -> str:
        n = len(stoneValue)

        # the optimal stone difference any player can take more than the opponent.
        dp = [0] * 3

        for i in range(n-1, -1, -1):
            # take one stone = take only stoneValue[i] - next opponent's optimal diff.
            take_one = stoneValue[i] - dp[(i+1) % 3]

            take_two = take_three = float('-inf')
            # take 2 stones = take stoneValue[i:i+2] - next opponent's optimal diff.
            if i + 1 < n:
                take_two = stoneValue[i] + stoneValue[i+1] - dp[(i+2) % 3]
            # take 3 stones = take stoneValue[i:i+3] - next opponent's optimal diff. (dp[(i+3)%3] == dp[i%3])
            if i + 2 < n:
                take_three = stoneValue[i] + stoneValue[i+1] + stoneValue[i+2] - dp[i % 3]

            # maximize the optimal move
            dp[i % 3] = max(take_one, take_two, take_three)

        first_move = dp[0]  # by Alice
        if first_move > 0:
            return "Alice"
        elif first_move < 0:
            return "Bob"
        else:
            return "Tie"

