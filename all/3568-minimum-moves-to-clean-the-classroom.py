'''
2026/09/01 daily challenge

breadth first search approach

Runtime=2316ms, Beats 45.61%
'''


import collections


class Solution:
    def minMoves(self, classroom: List[str], energy: int) -> int:
        n, m = len(classroom), len(classroom[0])
        litter2idx = dict()
        litter_count = 0
        start = None

        for i, row in enumerate(classroom):
            for j, cell in enumerate(row):
                if cell == 'L':
                    litter2idx[(i, j)] = litter_count
                    litter_count += 1
                elif cell == 'S':
                    start = (i, j)

        # dp[i][j][remaining_litter_bitmask] = remaining_energy
        dp = [[dict() for _ in range(m)] for _ in range(n)]

        # status = [moves, x, y, remaining_litter_bitmask, remaining_energy]
        q = collections.deque([[0, start[0], start[1], (1 << litter_count) - 1, energy]])
        while q:
            moves, x, y, mask, k = q.popleft()
            cell = classroom[x][y]
            if cell == 'L' and mask & (1 << litter2idx[(x, y)]):
                mask -= 1 << litter2idx[(x, y)]
            if mask == 0:
                # all litter collected
                return moves
            if cell == 'R':
                k = energy
            elif k == 0:
                # out of energy
                continue
            if k <= dp[x][y].get(mask, 0):
                # already visited with the same state
                continue
            dp[x][y][mask] = k
            # print("(%d, %d, %s)" % (x, y, bin(mask)))

            # move to adjacent cell
            moves += 1
            k -= 1
            for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                dx += x
                dy += y
                if 0 <= dx < n and 0 <= dy < m and classroom[dx][dy] != 'X':
                    q.append([moves, dx, dy, mask, k])
        # impossible to clean all litter up
        return -1

