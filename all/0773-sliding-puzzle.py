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


'''
level order traversal approach (BFS)

runtime=4ms
'''


import collections


class Solution:
    def slidingPuzzle(self, board: List[List[int]]) -> int:
        # convert the board to an 1-D array
        # and predefine each cell's next hop.
        '''
        +---+---+---+
        | 0 | 1 | 2 |    +---+---+---+---+---+---+
        +---+---+---+ => | 0 | 1 | 2 | 3 | 4 | 5 |
        | 3 | 4 | 5 |    +---+---+---+---+---+---+
        +---+---+---+
        '''
        next_hops = {0: [1, 3],
                     1: [0, 4, 2],
                     2: [1, 5],
                     3: [0, 4],
                     4: [3, 1, 5],
                     5: [4, 2]}

        goal = (1, 2, 3, 4, 5, 0)

        q = collections.deque()
        x = y = -1
        # search the starting point 0
        for i, row in enumerate(board):
            for j, cell in enumerate(row):
                if cell == 0:
                    x, y = i, j
                    break
            if x != -1:
                break
        q.append((x*3 + y, board[0] + board[1]))

        # level order BFS
        step = 0
        seen = set()
        while q:
            width = len(q)
            for _ in range(width):
                idx, state = q.popleft()
                key = tuple(state)
                if key in seen:
                    continue
                if key == goal:
                    return step
                seen.add(key)

                # queue deeper
                for next_idx in next_hops[idx]:
                    next_state = state.copy()
                    next_state[idx], next_state[next_idx] = next_state[next_idx], next_state[idx]
                    q.append((next_idx, next_state))
            step += 1

        return -1

