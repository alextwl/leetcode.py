'''
2023/01/31 daily challenge

dynamic programming approach (iterative bottom-up ver)
'''


class Solution:
    def bestTeamScore(self, scores: List[int], ages: List[int]) -> int:
        players = list(zip(ages, scores))
        '''
        sort players by ages & scores in ascending order.
        this gurarntees when we iterate the pairs,
        the current player's age is always equal to or greater than the previous,
        or its score is equal to or greater than the previous in the same age.

        so that we can build the overall highest score in bottom-up approach.
        '''
        players.sort()
        '''
        dp[i] = the maximum score if i-th player selected.
        initialized with only i-th player itself selected (== its own score.)
        '''
        dp = [score for _, score in players]
        ans = max(dp)  # the overall highest score

        for i in range(0, len(players)):
            for j in range(i-1, -1, -1):
                '''
                if i-th player's score is higher than a previous j-th player's,
                we may select i-th player in the following cases:

                (1) the team with i-th player selected. (the team built before is inherited.)
                (2) the team with i-th player selected when j-th player is explicitly already in.

                and then choose the maximum score for the team with i-th player.
                '''
                if players[i][1] >= players[j][1]:
                    dp[i] = max(dp[i], dp[j] + players[i][1])
            # update the overall highest score whether i-th player is in or not.
            ans = max(ans, dp[i])

        return ans

