'''
2024/10/31 daily challenge

dynamic programming approach (recursive ver)

note using functools.cache will exceed the memory limit,
allocate the dp space manually.

learnt from official solution:
https://leetcode.com/problems/minimum-total-distance-traveled/solution/

also see the analysis in the Approach 1 for "Why Does Sorting Always Work?"
it explains several cases on different pairs of two robots and two factories
and finds in all cases assigning a robot with a nearest available factory
is always optimal.
'''


class Solution:
    def minimumTotalDistance(self, robot: List[int], factory: List[List[int]]) -> int:
        robot.sort()
        factory.sort()
        factorypos = []

        # flatten the positions of all factories.
        for pos, limit in factory:
            factorypos.extend([pos] * limit)

        m, n = len(robot), len(factorypos)
        
        dp = [[None] * (n + 1) for _ in range(m + 1)]
        
        def solve(robot_idx, factory_idx):
            if dp[robot_idx][factory_idx] is not None:
                return dp[robot_idx][factory_idx]
            if robot_idx == m:
                dp[robot_idx][factory_idx] = 0
                return 0
            if factory_idx == n:
                dp[robot_idx][factory_idx] = float('inf')
                return float('inf')

            # let the robot repair at this factory
            repair_here = abs(robot[robot_idx] - factorypos[factory_idx]) + \
                            solve(robot_idx + 1, factory_idx + 1)

            # skip this factory
            goto_next_factory = solve(robot_idx, factory_idx + 1)

            dp[robot_idx][factory_idx] = min(repair_here, goto_next_factory)
            return dp[robot_idx][factory_idx]

        return solve(0, 0)


'''
bottom-up dynamic programming approach (iterative ver)
'''


class Solution:
    def minimumTotalDistance(self, robot: List[int], factory: List[List[int]]) -> int:
        robot.sort()
        factory.sort()
        factorypos = []

        # flatten the positions of all factories.
        for pos, limit in factory:
            factorypos.extend([pos] * limit)

        m, n = len(robot), len(factorypos)

        # dp[i][j] = the minimum moves for robot_i and factory_j pair.
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        for row in dp:
            # out of available factories
            row[-1] = float('inf')
        # base case, when no both robot & factory left, the necessary move is zero.
        dp[-1][-1] = 0

        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                repair_here = abs(robot[i] - factorypos[j]) + dp[i+1][j+1]
                goto_next_factory = dp[i][j+1]
                dp[i][j] = min(repair_here, goto_next_factory)

        return dp[0][0]

