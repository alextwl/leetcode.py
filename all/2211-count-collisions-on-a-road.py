'''
2025/12/04 daily challenge

counter approach
'''


class Solution:
    def countCollisions(self, directions: str) -> int:
        r = s = 0
        ans = 0

        for c in directions:
            if c == 'L':
                if r:
                    # 2 collisions: the current car collides with
                    # the rightmost car moving in right direction.
                    # (r - 1) collisions: remaining cars moving in right direction
                    # collide with a stationary car collided previously.
                    ans += r + 1
                    r = 0
                    s = 1  # so we have a stationary car here
                elif s:
                    ans += 1
            elif c == 'R':
                s = 0  # the previous stationary car is no longer relevant.
                r += 1
            else:
                # c == 'S'
                # we have a stationary car now,
                # collides with previous cars moving in the right directions.
                ans += r
                r = 0
                s = 1
        return ans


'''
two-liner ver

learnt from official editorial 2:
https://leetcode.com/problems/count-collisions-on-a-road/editorial/#approach-2-counting

all vehicles other than leftmost Ls & rightmost Rs will collide exactly once.
'''


class Solution:
    def countCollisions(self, directions: str) -> int:
        arr = directions.lstrip('L').rstrip('R')
        return len(arr) - arr.count('S')

