'''
2024/11/25 daily challenge

backtrace approach (brute force because the input is small enough.)
'''


import collections


class Solution:
    def slidingPuzzle(self, board: List[List[int]]) -> int:
        goal = (1, 2, 3, 4, 5, 0)
        min_steps = collections.defaultdict(lambda: float('inf'))
        
        def backtrace(x, y, step):
            key = tuple(board[0] + board[1])

            if key == goal:
                # goal achieved
                min_steps[key] = min(min_steps[key], step)
                return
            if min_steps[key] <= step:
                # same or smaller ans already found, no need to search further
                return
            min_steps[key] = step
            
            step += 1
            for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                dx += x
                dy += y
                if 0 <= dx < 2 and 0 <= dy < 3:
                    # swap
                    board[x][y], board[dx][dy] = board[dx][dy], board[x][y]
                    backtrace(dx, dy, step)
                    # recover
                    board[x][y], board[dx][dy] = board[dx][dy], board[x][y]
            return
        
        x = y = -1
        # find the starting point 0
        for i, row in enumerate(board):
            for j, v in enumerate(row):
                if v == 0:
                    x, y = i, j
                    break
            if x != -1:
                break
        backtrace(x, y, 0)

        return min_steps.get(goal, -1)

