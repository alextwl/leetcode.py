'''
leetcode 75 lv2 day 10

breadth first search approach

simultaneously rot oranges near to all rotten oranges in the beginning,
and the answer will be guaranteed the minimum number of minutes.

the problem does not limit us to start from any rotten oranges.
'''

import collections


class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        # count oranges
        oranges = 0
        rottens = 0  # counter of rotten oranges
        q = collections.deque()  # FIFO queue to check rotten oranges
        for x, row in enumerate(grid):
            for y, cell in enumerate(row):
                if cell:
                    oranges += 1
                if cell == 2:
                    q.append((x, y))

        minutes = 0
        # BFS from all rotten oranges in the beginning
        while(q):
            # count current rottens to be checked
            currents = len(q)
            rottens += currents
            while(currents):
                currents -= 1
                x, y = q.popleft()
                for dx, dy in [(1,0), (-1,0), (0,-1), (0,1)]:
                    nx, ny = x+dx, y+dy
                    if 0 <= nx < len(grid) and 0 <= ny < len(grid[0]) and grid[nx][ny] == 1:
                        # rot the orange
                        grid[nx][ny] = 2
                        q.append((nx, ny))
            if q:
                minutes += 1

        if oranges == rottens:
            return minutes

        return -1

