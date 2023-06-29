'''
2023/06/29 daily challenge

breadth first search approach
'''

import collections
from string import ascii_lowercase as lower, ascii_uppercase as upper


class Solution:
    def shortestPathAllKeys(self, grid: List[str]) -> int:
        total_keys = 0

        def char2cell(c: str):
            nonlocal total_keys

            if c == '.':
                return 0
            if c == '#':
                return -1
            if c == '@':
                return 0
            
            chex = ord(c)
            if chex <= 90:
                # it's a locker.
                # == (1 << (ord(c) - ord('A') + 1)) | 1
                # the leftmost bit is locker bit.
                return (1 << (chex - 64)) | 1

            total_keys += 1
            # it's a key.
            # == 1 << (1 << (ord(c) - ord('a') + 1))
            # the leftmost bit is non-locker bit.
            return 1 << (chex - 96)

        m = len(grid)
        n = len(grid[0])
        '''
        g[(i, j)] = cell bitmask
        '''
        g = dict()

        # convert grid and search starting point
        start = None
        for i, row in enumerate(grid):
            for j, cell in enumerate(row):
                if cell == '@':
                    start = (i, j)
                    # print("start at %s" % str(start))
                    g[(i, j)] = 0
                else:
                    g[(i, j)] = char2cell(cell)

        seen = collections.defaultdict(dict)  # memorize shortest path len for all key combinations for each cell
        ans = float('inf')

        # print('total_keys=%d' % total_keys)

        # q = [(i, j, key_obtained, path len)]
        q = collections.deque([(start[0], start[1], 0, 0)])
        # BFS
        while(q):
            i, j, key_obtained, path_len = q.popleft()
            cell_bit = g[(i, j)]

            if path_len > ans:
                # ans minimized, no need to traverse longer
                continue

            if cell_bit < 0:
                # it's a wall
                continue
            if cell_bit & 1 and not (cell_bit & (key_obtained << 1)):
                # it's a locker and cannot be unlocked
                continue

            # retrieve the key (if available)
            if not(cell_bit & 1):
                key_obtained = key_obtained | (cell_bit >> 1)

            cell_path_len = seen[(i, j)].get(key_obtained, float('inf'))
            if path_len >= cell_path_len:
                # the path len is not shorter for the same key combination
                continue

            # visit the cell & update the path len
            seen[(i, j)][key_obtained] = path_len
            
            if key_obtained.bit_count() == total_keys:
                # all keys found
                ans = min(ans, path_len)
                continue

            # queue the neighbors
            path_len += 1
            for x, y in [(1, 0), (-1, 0), (0, -1), (0, 1)]:
                x += i
                y += j
                if 0 <= x < m and 0 <= y < n:
                    q.append((x, y, key_obtained, path_len))

        return -1 if ans == float('inf') else ans

