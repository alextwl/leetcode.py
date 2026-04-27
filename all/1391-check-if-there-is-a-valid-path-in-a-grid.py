'''
2026/04/27 daily challenge

breadth first search approach
'''


import collections


'''
exit/entrance side number by direction:

    1
  +---+
0 |   | 2
  +---+
    3
'''


# street type to exits/entrances
ST2EXIT = {1: [0, 2], 2: [1, 3], 3: [0, 3], 4: [2, 3], 5: [0, 1], 6: [1, 2]}
# entrance to street type
ENT2ST = {0: {1, 3, 5}, 1: {2, 5, 6}, 2: {1, 4, 6}, 3: {2, 3, 4}}
# exit deltas
EXIT_DELTA = [(0, -1), (-1, 0), (0, 1), (1, 0)]
# exit to entrance
EXIT2ENT = [2, 3, 0, 1]


class Solution:
    def hasValidPath(self, grid: List[List[int]]) -> bool:
        m, n = len(grid), len(grid[0])
        m1, n1 = m - 1, n - 1

        if m1 == 0 and n1 == 0:
            # corner case: the beginning is the destination.
            return True

        seen = set()
        q = collections.deque([(0, 0, -1)])  # (x, y, side where entered from)
        while q:
            x, y, src = q.popleft()

            node = (x, y)
            if node in seen:
                continue
            seen.add(node)

            # get street type of current cell
            stype = grid[x][y]
            # check exits
            for exit_side in ST2EXIT[stype]:
                if exit_side == src:
                    # cannot exit from incoming side
                    continue
                # get coordinate of next cell
                dx, dy = EXIT_DELTA[exit_side]
                dx, dy = dx + x, dy + y
                # set the entrance number of next cell
                next_src = EXIT2ENT[exit_side]
                # boundary check & entrance check
                if 0 <= dx < m and 0 <= dy < n and next_src in ST2EXIT[grid[dx][dy]]:
                    if dx == m1 and dy == n1:
                        # destination arrived
                        return True
                    q.append((dx, dy, next_src))
        return False

