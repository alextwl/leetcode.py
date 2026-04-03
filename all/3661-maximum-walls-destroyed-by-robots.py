'''
2026/04/03 daily challenge

sorting + dynamic programming + enumeration approach
'''


class Solution:
    def maxWalls(self, robots: List[int], distance: List[int], walls: List[int]) -> int:
        # add dummy terminals with zero distance (cannot fire)
        robots.append(-1)
        robots.append(1_000_000_007)
        distance.append(0)
        distance.append(0)
        # build sorted map from element to index of robots & distance
        pos2idx = list(range(len(robots)))
        pos2idx.sort(key=robots.__getitem__)
        # sort walls by its positions
        walls.sort()

        dp = [0] * 4
        curr = 0
        left, right = pos2idx[0], pos2idx[1]
        for i, wall_pos in enumerate(walls):
            # search next wall between two robots
            while wall_pos > robots[right]:
                curr += 1
                left, right = pos2idx[curr], pos2idx[curr + 1]
                max_left, max_right = max(dp[0], dp[2]), max(dp[1], dp[3])
                dp[0] = dp[1] = max_left
                dp[2] = dp[3] = max_right
            # wall <-- right robot
            if wall_pos >= robots[right] - distance[right]:
                dp[0] += 1
            # wall <-- right robot when wall and robot are together
            if wall_pos == robots[right]:
                dp[1] += 1
            # left robot --> wall
            # right robot --> wall
            if (wall_pos <= robots[left] + distance[left]) or \
                    (wall_pos >= robots[right] - distance[right]):
                dp[2] += 1
            # left robot --> wall
            # right robot --> wall when wall and robot are together
            if (wall_pos <= robots[left] + distance[left]) or \
                    (wall_pos == robots[right]):
                dp[3] += 1

        return max(dp)

