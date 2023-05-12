'''
2023/05/12 daily challenge

dynamic programming approach (bottom-up)

the idea is similar to house robber but the distances of jumps are vary.
'''

class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        n = len(questions)
        dp = [0] * (n+1)  # dp[i] = the max points can be earned at i-th question reversely.

        for i in range(n-1, -1, -1):
            points, brainpower = questions[i]

            '''
            find the right-side nearest question's **max** points
            and add it into current earned points.

            For example 1:
            (1) when i=3, although it costs brainpower=5
                and the next question is expected i=10 (unable to solve i=4~9),
                there's no i=10 question actually,
                so we accumulate points from the base case dp[n], which is 0.
            (2) when i=0, it costs brainpower=2
                and the next question is i=3 (unable to solve i=1~2),
                the current max points are questions[0] + dp[3]
                because question i=3 is the nearest question we can jump from i=0.
            '''
            points += dp[min(n, i+brainpower+1)]

            '''
            we have choices to decide whether we are going to solve i or not,
            to maximize the result, we select the bigger one between:
            (1) solve the current question to earn points we've calculated before,
            (2) or just skip it, the max points earned are inherited from dp[i+1].
            '''
            dp[i] = max(points, dp[i+1])

        return dp[0]

